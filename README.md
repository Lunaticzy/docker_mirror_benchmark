# Docker Mirror Benchmark

🚀 自动生成的镜像源速度排行榜 (更新于 2025-06-14 03:03:30)

## 测试镜像
- 镜像名称: `library/nginx:latest`
- 测试架构: `amd64`
- 测试数据量: `10MB`

## 速度排行榜
| 排名 | 镜像源地址 | 平均下载速度 |
|------|------------|--------------|
| 1 | `a.ussh.net` | 4.26 MB/s |
| 2 | `docker-0.unsee.tech` | 4.07 MB/s |
| 3 | `docker.melikeme.cn` | 3.70 MB/s |
| 4 | `docker.xuanyuan.me` | 2.11 MB/s |
| 5 | `docker.hlmirror.com` | 1.88 MB/s |
| 6 | `lispy.org` | 1.54 MB/s |
| 7 | `docker-mirror.aigc2d.com` | 0.69 MB/s |
| 8 | `docker.kejilion.pro` | 0.05 MB/s |

## 配置

```json
{
  "registry-mirrors": [
    "https://a.ussh.net",
    "https://docker-0.unsee.tech",
    "https://docker.melikeme.cn",
    "https://docker.xuanyuan.me",
    "https://docker.hlmirror.com"
  ],
  "features": {
    "buildkit": true
  },
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "100m",
    "max-file": "3"
  }
}
```

## 配置说明
生成的配置文件已包含以下优化策略：
- 前5个最快镜像源
- 日志配置优化

