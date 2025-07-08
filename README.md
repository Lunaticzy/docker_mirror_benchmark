# Docker Mirror Benchmark

🚀 自动生成的镜像源速度排行榜 (更新于 2025-07-09 03:00:31)

## 测试镜像
- 镜像名称: `library/nginx:latest`
- 测试架构: `amd64`
- 测试数据量: `10MB`

## 速度排行榜
| 排名 | 镜像源地址 | 平均下载速度 |
|------|------------|--------------|
| 1 | `lispy.org` | 4.57 MB/s |
| 2 | `docker.xiaogenban1993.com` | 4.32 MB/s |
| 3 | `docker.1panel.live` | 4.08 MB/s |
| 4 | `docker.melikeme.cn` | 3.93 MB/s |
| 5 | `docker.xuanyuan.me` | 3.92 MB/s |
| 6 | `docker.hlmirror.com` | 3.64 MB/s |
| 7 | `docker.kejilion.pro` | 0.87 MB/s |
| 8 | `docker-0.unsee.tech` | 0.85 MB/s |
| 9 | `docker-mirror.aigc2d.com` | 0.59 MB/s |

## 配置

```json
{
  "registry-mirrors": [
    "https://lispy.org",
    "https://docker.xiaogenban1993.com",
    "https://docker.1panel.live",
    "https://docker.melikeme.cn",
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

