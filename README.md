# Docker Mirror Benchmark

🚀 自动生成的镜像源速度排行榜 (更新于 2025-07-13 03:00:27)

## 测试镜像
- 镜像名称: `library/nginx:latest`
- 测试架构: `amd64`
- 测试数据量: `10MB`

## 速度排行榜
| 排名 | 镜像源地址 | 平均下载速度 |
|------|------------|--------------|
| 1 | `lispy.org` | 3.11 MB/s |
| 2 | `docker.hlmirror.com` | 2.28 MB/s |
| 3 | `docker.kejilion.pro` | 0.96 MB/s |
| 4 | `docker-mirror.aigc2d.com` | 0.78 MB/s |
| 5 | `docker-0.unsee.tech` | 0.69 MB/s |

## 配置

```json
{
  "registry-mirrors": [
    "https://lispy.org",
    "https://docker.hlmirror.com",
    "https://docker.kejilion.pro",
    "https://docker-mirror.aigc2d.com",
    "https://docker-0.unsee.tech"
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

