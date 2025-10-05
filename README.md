# Docker Mirror Benchmark

🚀 自动生成的镜像源速度排行榜 (更新于 2025-10-06 03:00:26)

## 测试镜像
- 镜像名称: `library/nginx:latest`
- 测试架构: `amd64`
- 测试数据量: `10MB`

## 速度排行榜
| 排名 | 镜像源地址 | 平均下载速度 |
|------|------------|--------------|
| 1 | `lispy.org` | 4.91 MB/s |
| 2 | `docker.1panel.live` | 4.44 MB/s |
| 3 | `docker-0.unsee.tech` | 3.89 MB/s |
| 4 | `docker-mirror.aigc2d.com` | 0.64 MB/s |

## 配置

```json
{
  "registry-mirrors": [
    "https://lispy.org",
    "https://docker.1panel.live",
    "https://docker-0.unsee.tech",
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

