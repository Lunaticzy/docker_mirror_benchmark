# Docker Mirror Benchmark

🚀 自动生成的镜像源速度排行榜 (更新于 2025-06-26 03:00:31)

## 测试镜像
- 镜像名称: `library/nginx:latest`
- 测试架构: `amd64`
- 测试数据量: `10MB`

## 速度排行榜
| 排名 | 镜像源地址 | 平均下载速度 |
|------|------------|--------------|
| 1 | `docker-0.unsee.tech` | 3.07 MB/s |
| 2 | `docker.melikeme.cn` | 1.68 MB/s |
| 3 | `docker.xuanyuan.me` | 0.82 MB/s |
| 4 | `docker.kejilion.pro` | 0.61 MB/s |
| 5 | `lispy.org` | 0.58 MB/s |
| 6 | `docker-mirror.aigc2d.com` | 0.57 MB/s |
| 7 | `docker.hlmirror.com` | 0.55 MB/s |

## 配置

```json
{
  "registry-mirrors": [
    "https://docker-0.unsee.tech",
    "https://docker.melikeme.cn",
    "https://docker.xuanyuan.me",
    "https://docker.kejilion.pro",
    "https://lispy.org"
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

