# Docker Mirror Benchmark

🚀 自动生成的镜像源速度排行榜 (更新于 2025-05-16 03:00:32)

## 测试镜像
- 镜像名称: `library/nginx:latest`
- 测试架构: `amd64`
- 测试数据量: `10MB`

## 速度排行榜
| 排名 | 镜像源地址 | 平均下载速度 |
|------|------------|--------------|
| 1 | `docker.1panel.live` | 5.40 MB/s |
| 2 | `docker-0.unsee.tech` | 4.26 MB/s |
| 3 | `a.ussh.net` | 4.04 MB/s |
| 4 | `docker.xuanyuan.me` | 3.20 MB/s |
| 5 | `docker.mybacc.com` | 3.01 MB/s |
| 6 | `docker.xiaogenban1993.com` | 2.95 MB/s |
| 7 | `docker.melikeme.cn` | 2.39 MB/s |
| 8 | `lispy.org` | 2.01 MB/s |
| 9 | `docker.hlmirror.com` | 1.58 MB/s |
| 10 | `docker-mirror.aigc2d.com` | 0.52 MB/s |

## 配置

```json
{
  "registry-mirrors": [
    "https://docker.1panel.live",
    "https://docker-0.unsee.tech",
    "https://a.ussh.net",
    "https://docker.xuanyuan.me",
    "https://docker.mybacc.com"
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

