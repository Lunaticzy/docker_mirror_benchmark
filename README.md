# Docker Mirror Benchmark

🚀 自动生成的镜像源速度排行榜 (更新于 2025-06-11 03:00:57)

## 测试镜像
- 镜像名称: `library/nginx:latest`
- 测试架构: `amd64`
- 测试数据量: `10MB`

## 速度排行榜
| 排名 | 镜像源地址 | 平均下载速度 |
|------|------------|--------------|
| 1 | `docker.melikeme.cn` | 3.31 MB/s |
| 2 | `a.ussh.net` | 2.07 MB/s |
| 3 | `docker.1panel.live` | 1.35 MB/s |
| 4 | `docker.hlmirror.com` | 1.34 MB/s |
| 5 | `docker.xuanyuan.me` | 1.15 MB/s |
| 6 | `lispy.org` | 1.02 MB/s |
| 7 | `docker-mirror.aigc2d.com` | 0.61 MB/s |
| 8 | `docker.kejilion.pro` | 0.23 MB/s |

## 配置

```json
{
  "registry-mirrors": [
    "https://docker.melikeme.cn",
    "https://a.ussh.net",
    "https://docker.1panel.live",
    "https://docker.hlmirror.com",
    "https://docker.xuanyuan.me"
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

