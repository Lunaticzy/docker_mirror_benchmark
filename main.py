import sys
import re
import json
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# 配置参数
DEFAULT_MIRROR = "https://hub.docker.lnatic.icu"
TEST_IMAGE = "library/nginx"
TEST_TAG = "latest"
TEST_ARCH = "amd64"
USER_AGENT = "DockerMirrorTester/1.0"
MIN_LAYER_SIZE = 10 * 1024 * 1024  # 10MB
TEST_DATA_SIZE = 10 * 1024 * 1024  # 测试数据量
CHUNK_SIZE = 1024 * 64  # 64KB
MAX_WORKERS = 10
CACHE_EXPIRE = 300  # 认证缓存时间(秒)
MIN_AVAILABILITY = 95.0


class RegistryAuth:
    def __init__(self):
        self.session = requests.Session()
        self.auth_cache = {}
        self._setup_session()

    def _setup_session(self):
        """配置会话重试策略"""
        retry = Retry(
            total=3,
            backoff_factor=0.5,
            status_forcelist=[500, 502, 503, 504]
        )
        adapter = HTTPAdapter(max_retries=retry)
        self.session.mount('http://', adapter)
        self.session.mount('https/', adapter)

    def parse_auth_header(self, header):
        """解析WWW-Authenticate头"""
        return dict(re.findall(r'(\w+)="([^"]+)"', header))

    def get_registry_token(self, auth_info, repository):
        """获取并缓存Registry Token"""
        cache_key = f"{auth_info['realm']}|{repository}"
        cached = self.auth_cache.get(cache_key)

        if cached and time.time() - cached['timestamp'] < CACHE_EXPIRE:
            return cached['token']

        try:
            params = {
                "service": auth_info.get('service', 'registry.docker.io'),
                "scope": f"repository:{repository}:pull"
            }
            resp = self.session.get(auth_info['realm'], params=params, timeout=5)
            resp.raise_for_status()
            token_data = resp.json()

            self.auth_cache[cache_key] = {
                'token': token_data['token'],
                'timestamp': time.time()
            }
            return token_data['token']
        except Exception as e:
            print(f"🔑 认证失败: {str(e)}")
            return None


def fetch_mirror_list():
    """获取镜像源候选列表"""
    print("🕸️ 正在获取镜像源列表...")
    try:
        resp = requests.get("https://tools.opsnote.top/registry-mirrors/", timeout=10)
        soup = BeautifulSoup(resp.text, 'html.parser')

        mirrors = []
        for item in soup.find_all('div', class_='target-container'):
            url_tag = item.find('h2')
            if not url_tag: continue

            status_tags = item.find_all('div', class_='status-value')
            if len(status_tags) < 3: continue

            try:
                availability = [float(tag.text.strip('%')) for tag in status_tags[:3]]
                if min(availability) >= MIN_AVAILABILITY:
                    mirrors.append(url_tag.text.strip())
            except ValueError:
                continue

        return [urlparse(m).geturl().rstrip('/') for m in mirrors]
    except Exception as e:
        print(f"⚠️ 镜像源列表获取失败: {str(e)}")
        return []


def get_test_layer_digest(auth_handler):
    """获取用于测试的Layer摘要"""
    print("\n🔍 正在选择测试层...")
    try:
        registry = "registry-1.docker.io"
        repository = TEST_IMAGE
        tag = TEST_TAG

        # 获取镜像清单
        manifest_url = f"https://{registry}/v2/{repository}/manifests/{tag}"
        headers = {'Accept': 'application/vnd.docker.distribution.manifest.v2+json'}
        resp = auth_handler.session.get(manifest_url, headers=headers)

        # 处理401认证
        if resp.status_code == 401:
            auth_header = resp.headers.get('WWW-Authenticate', '')
            auth_info = auth_handler.parse_auth_header(auth_header)
            token = auth_handler.get_registry_token(auth_info, repository)
            if not token:
                raise PermissionError("无法获取访问令牌")
            headers['Authorization'] = f'Bearer {token}'
            resp = auth_handler.session.get(manifest_url, headers=headers)

        resp.raise_for_status()
        data = resp.json()

        # 处理多架构镜像
        if 'manifests' in data:
            for manifest in data['manifests']:
                platform = manifest.get('platform', {})
                if platform.get('architecture') == TEST_ARCH and platform.get('os') == 'linux':
                    digest = manifest['digest']
                    # 获取架构特定清单
                    manifest_url = f"https://{registry}/v2/{repository}/manifests/{digest}"
                    resp = auth_handler.session.get(manifest_url, headers=headers)
                    data = resp.json()
                    break

        # 选择符合条件的Layer
        candidate = None
        for layer in data.get('layers', []):
            if layer['size'] >= MIN_LAYER_SIZE:
                candidate = layer
                break

        # 没有符合条件的则选择最大层
        if not candidate:
            candidate = max(data['layers'], key=lambda x: x['size'])
            print(f"⚠️ 没有足够大的层，使用最大层 ({candidate['size'] // 1024 // 1024}MB)")
        else:
            print(f"✅ 选定测试层 ({candidate['size'] // 1024 // 1024}MB)")

        return candidate['digest']
    except Exception as e:
        print(f"❌ 层选择失败: {str(e)}")
        sys.exit(1)


def test_mirror(auth_handler, mirror_url, layer_digest):
    """测试单个镜像源性能（无进度条版）"""
    try:
        test_url = f"{mirror_url}/v2/{TEST_IMAGE}/blobs/{layer_digest}"
        headers = {'User-Agent': USER_AGENT}
        cache_key = f"{mirror_url}|{TEST_IMAGE}"

        def handle_401(response):
            """统一处理401认证流程"""
            nonlocal headers
            auth_header = response.headers.get('WWW-Authenticate', '')
            if not auth_header:
                return False

            auth_info = auth_handler.parse_auth_header(auth_header)
            token = auth_handler.get_registry_token(auth_info, TEST_IMAGE)
            if not token:
                return False

            headers['Authorization'] = f'Bearer {token}'
            auth_handler.auth_cache[cache_key] = {
                'token': token,
                'timestamp': time.time()
            }
            return True

        # 第一次HEAD请求获取文件大小
        resp = auth_handler.session.head(test_url, headers=headers, timeout=5)
        if resp.status_code == 401 and handle_401(resp):
            resp = auth_handler.session.head(test_url, headers=headers, timeout=5)
        resp.raise_for_status()

        # 处理文件大小
        total_size = int(resp.headers.get('content-length', 0))
        download_size = min(total_size, TEST_DATA_SIZE)
        if download_size < 1024 * 1024:
            return mirror_url, 0.0, False

        # 准备下载参数
        headers['Range'] = f'bytes=0-{download_size - 1}'
        start_time = time.time()
        downloaded = 0

        # 静默下载
        with auth_handler.session.get(
                test_url,
                headers=headers,
                stream=True,
                timeout=15
        ) as resp:
            # 处理下载时的401
            if resp.status_code == 401 and handle_401(resp):
                resp = auth_handler.session.get(
                    test_url,
                    headers=headers,
                    stream=True,
                    timeout=15
                )
            resp.raise_for_status()

            # 分块下载
            for chunk in resp.iter_content(chunk_size=CHUNK_SIZE):
                if chunk:  # 过滤keep-alive chunks
                    downloaded += len(chunk)
                    if downloaded >= download_size:
                        break

        # 计算速度（保留两位小数）
        duration = max(time.time() - start_time, 0.001)  # 防止除以0
        speed = round((downloaded / 1024 / 1024) / duration, 2)
        return mirror_url, speed, True

    except Exception as e:
        print(f"{mirror_url} 测试失败: {str(e)}")
        return mirror_url, 0.0, False


def generate_markdown_table(mirrors):
    """生成Markdown表格"""
    if not mirrors:
        return "⚠️ 当前没有可用的镜像源数据"

    table = [
        "| 排名 | 镜像源地址 | 平均下载速度 |",
        "|------|------------|--------------|"
    ]

    for idx, (url, speed, _) in enumerate(mirrors[:10], 1):
        hostname = urlparse(url).netloc
        table.append(f"| {idx} | `{hostname}` | {speed:.2f} MB/s |")

    return '\n'.join(table)

# 添加新的生成README函数
def generate_readme(ranked_mirrors):
    """生成包含速度排行的README.md"""
    readme_content = f"""# Docker Mirror Benchmark

🚀 自动生成的镜像源速度排行榜 (更新于 {time.strftime('%Y-%m-%d %H:%M:%S')})

## 测试镜像
- 镜像名称: `{TEST_IMAGE}:{TEST_TAG}`
- 测试架构: `{TEST_ARCH}`
- 测试数据量: `{TEST_DATA_SIZE//1024//1024}MB`

## 速度排行榜
{generate_markdown_table(ranked_mirrors)}

## 配置说明
生成的配置文件已包含以下优化策略：
- 前5个最快镜像源
- 日志配置优化

"""

def main():
    auth_handler = RegistryAuth()

    # 获取测试层摘要
    layer_digest = get_test_layer_digest(auth_handler)

    # 获取镜像源列表
    mirrors = fetch_mirror_list()
    mirrors.append(DEFAULT_MIRROR)

    # 执行性能测试
    print(f"\n🚀 开始测试 {len(mirrors)} 个镜像源...")
    results = []
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = [executor.submit(test_mirror, auth_handler, m, layer_digest) for m in mirrors]

        for future in tqdm(as_completed(futures), total=len(futures), desc="测试进度"):
            results.append(future.result())

    # 处理结果
    valid_mirrors = sorted(
        [r for r in results if r[2] and r[1] > 0],
        key=lambda x: -x[1]
    )

    # 输出结果
    print("\n🏆 速度排行榜 (MB/s):")
    for i, (url, speed, _) in enumerate(valid_mirrors[:10], 1):
        print(f"{i:2d}. {urlparse(url).netloc:<25} {speed:.2f} MB/s")

    # 生成配置文件
    top_mirrors = [m[0] for m in valid_mirrors[:5]]

    # # 确保默认源在最后
    # if DEFAULT_MIRROR in top_mirrors:
    #     top_mirrors.remove(DEFAULT_MIRROR)
    # top_mirrors.append(DEFAULT_MIRROR)

    config = {
        "registry-mirrors": top_mirrors,
        "features": {"buildkit": True},
        "log-driver": "json-file",
        "log-opts": {
            "max-size": "100m",
            "max-file": "3",
        }
    }
    with open('daemon.json', 'w') as f:
        json.dump(config, f, indent=2)

    print("\n✅ 配置文件已生成: daemon.json")
    print("🔄 请执行以下命令应用配置:")
    print(
        "sudo cp daemon.json /etc/docker/daemon.json && sudo systemctl daemon-reload && sudo systemctl restart docker")

if __name__ == "__main__":
    main()
