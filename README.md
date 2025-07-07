# Docker Mirror Benchmark

🚀 自动生成的镜像源速度排行榜 (更新于 2025-07-08 03:00:30)

## 测试镜像
- 镜像名称: `library/nginx:latest`
- 测试架构: `amd64`
- 测试数据量: `10MB`

## 速度排行榜
| 排名 | 镜像源地址 | 平均下载速度 |
|------|------------|--------------|
| 1 | `docker.xuanyuan.me` | 4.67 MB/s |
| 2 | `docker.melikeme.cn` | 3.53 MB/s |
| 3 | `lispy.org` | 2.95 MB/s |
| 4 | `docker.kejilion.pro` | 2.36 MB/s |
| 5 | `docker.1panel.live` | 1.98 MB/s |
| 6 | `docker.hlmirror.com` | 1.96 MB/s |
| 7 | `docker-0.unsee.tech` | 0.65 MB/s |

## 配置

```json
{
  "registry-mirrors": [
    "https://docker.xuanyuan.me",
    "https://docker.melikeme.cn",
    "https://lispy.org",
    "https://docker.kejilion.pro",
    "https://docker.1panel.live"
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

