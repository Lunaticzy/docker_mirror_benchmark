# Docker Mirror Benchmark

🚀 自动生成的镜像源速度排行榜 (更新于 2025-05-17 03:01:35)

## 测试镜像
- 镜像名称: `library/nginx:latest`
- 测试架构: `amd64`
- 测试数据量: `10MB`

## 速度排行榜
| 排名 | 镜像源地址 | 平均下载速度 |
|------|------------|--------------|
| 1 | `lispy.org` | 2.91 MB/s |
| 2 | `docker-0.unsee.tech` | 2.90 MB/s |
| 3 | `docker.1panel.live` | 2.74 MB/s |
| 4 | `docker.xiaogenban1993.com` | 2.01 MB/s |
| 5 | `a.ussh.net` | 1.19 MB/s |
| 6 | `docker.hlmirror.com` | 0.61 MB/s |
| 7 | `docker-mirror.aigc2d.com` | 0.53 MB/s |
| 8 | `docker.xuanyuan.me` | 0.48 MB/s |
| 9 | `docker.mybacc.com` | 0.17 MB/s |
| 10 | `docker.melikeme.cn` | 0.13 MB/s |

## 配置

```json
{
  "registry-mirrors": [
    "https://lispy.org",
    "https://docker-0.unsee.tech",
    "https://docker.1panel.live",
    "https://docker.xiaogenban1993.com",
    "https://a.ussh.net"
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

