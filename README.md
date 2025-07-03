# Docker Mirror Benchmark

🚀 自动生成的镜像源速度排行榜 (更新于 2025-07-04 03:00:25)

## 测试镜像
- 镜像名称: `library/nginx:latest`
- 测试架构: `amd64`
- 测试数据量: `10MB`

## 速度排行榜
| 排名 | 镜像源地址 | 平均下载速度 |
|------|------------|--------------|
| 1 | `docker.xuanyuan.me` | 2.21 MB/s |
| 2 | `docker.1panel.live` | 1.33 MB/s |
| 3 | `docker-0.unsee.tech` | 1.29 MB/s |
| 4 | `docker.hlmirror.com` | 1.24 MB/s |
| 5 | `docker.melikeme.cn` | 0.77 MB/s |
| 6 | `lispy.org` | 0.70 MB/s |
| 7 | `docker-mirror.aigc2d.com` | 0.68 MB/s |

## 配置

```json
{
  "registry-mirrors": [
    "https://docker.xuanyuan.me",
    "https://docker.1panel.live",
    "https://docker-0.unsee.tech",
    "https://docker.hlmirror.com",
    "https://docker.melikeme.cn"
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

