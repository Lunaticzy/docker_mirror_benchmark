# Docker Mirror Benchmark

🚀 自动生成的镜像源速度排行榜 (更新于 2025-05-18 22:17:16)

## 测试镜像
- 镜像名称: `library/nginx:latest`
- 测试架构: `amd64`
- 测试数据量: `10MB`

## 速度排行榜
| 排名 | 镜像源地址 | 平均下载速度 |
|------|------------|--------------|
| 1 | `docker-0.unsee.tech` | 1.67 MB/s |
| 2 | `docker.mybacc.com` | 1.60 MB/s |
| 3 | `docker.1panel.live` | 1.27 MB/s |
| 4 | `lispy.org` | 1.05 MB/s |
| 5 | `docker-mirror.aigc2d.com` | 0.50 MB/s |
| 6 | `a.ussh.net` | 0.48 MB/s |
| 7 | `docker.xiaogenban1993.com` | 0.45 MB/s |
| 8 | `docker.xuanyuan.me` | 0.36 MB/s |
| 9 | `docker.hlmirror.com` | 0.35 MB/s |
| 10 | `docker.melikeme.cn` | 0.02 MB/s |

## 配置

```json
{
  "registry-mirrors": [
    "https://docker-0.unsee.tech",
    "https://docker.mybacc.com",
    "https://docker.1panel.live",
    "https://lispy.org",
    "https://docker-mirror.aigc2d.com"
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

