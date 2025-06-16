# Docker Mirror Benchmark

🚀 自动生成的镜像源速度排行榜 (更新于 2025-06-17 03:00:40)

## 测试镜像
- 镜像名称: `library/nginx:latest`
- 测试架构: `amd64`
- 测试数据量: `10MB`

## 速度排行榜
| 排名 | 镜像源地址 | 平均下载速度 |
|------|------------|--------------|
| 1 | `docker.hlmirror.com` | 4.20 MB/s |
| 2 | `a.ussh.net` | 1.29 MB/s |
| 3 | `lispy.org` | 1.18 MB/s |
| 4 | `docker.xuanyuan.me` | 1.13 MB/s |
| 5 | `docker.melikeme.cn` | 1.04 MB/s |
| 6 | `docker-mirror.aigc2d.com` | 0.66 MB/s |
| 7 | `docker.kejilion.pro` | 0.34 MB/s |

## 配置

```json
{
  "registry-mirrors": [
    "https://docker.hlmirror.com",
    "https://a.ussh.net",
    "https://lispy.org",
    "https://docker.xuanyuan.me",
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

