# Docker Mirror Benchmark

🚀 自动生成的镜像源速度排行榜 (更新于 2025-07-07 03:01:48)

## 测试镜像
- 镜像名称: `library/nginx:latest`
- 测试架构: `amd64`
- 测试数据量: `10MB`

## 速度排行榜
| 排名 | 镜像源地址 | 平均下载速度 |
|------|------------|--------------|
| 1 | `docker.1panel.live` | 5.79 MB/s |
| 2 | `docker.kejilion.pro` | 3.47 MB/s |
| 3 | `docker.hlmirror.com` | 3.29 MB/s |
| 4 | `docker-0.unsee.tech` | 1.81 MB/s |
| 5 | `docker.melikeme.cn` | 1.05 MB/s |
| 6 | `docker.xuanyuan.me` | 0.27 MB/s |
| 7 | `lispy.org` | 0.10 MB/s |

## 配置

```json
{
  "registry-mirrors": [
    "https://docker.1panel.live",
    "https://docker.kejilion.pro",
    "https://docker.hlmirror.com",
    "https://docker-0.unsee.tech",
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

