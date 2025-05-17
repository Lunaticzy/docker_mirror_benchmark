# Docker Mirror Benchmark

🚀 自动生成的镜像源速度排行榜 (更新于 2025-05-18 03:00:27)

## 测试镜像
- 镜像名称: `library/nginx:latest`
- 测试架构: `amd64`
- 测试数据量: `10MB`

## 速度排行榜
| 排名 | 镜像源地址 | 平均下载速度 |
|------|------------|--------------|
| 1 | `docker.hlmirror.com` | 4.73 MB/s |
| 2 | `docker-0.unsee.tech` | 4.50 MB/s |
| 3 | `docker.1panel.live` | 4.17 MB/s |
| 4 | `lispy.org` | 3.25 MB/s |
| 5 | `docker.mybacc.com` | 3.21 MB/s |
| 6 | `a.ussh.net` | 2.60 MB/s |
| 7 | `docker.melikeme.cn` | 2.58 MB/s |
| 8 | `docker.xiaogenban1993.com` | 1.75 MB/s |
| 9 | `docker.xuanyuan.me` | 1.31 MB/s |
| 10 | `docker-mirror.aigc2d.com` | 0.61 MB/s |

## 配置

```json
{
  "registry-mirrors": [
    "https://docker.hlmirror.com",
    "https://docker-0.unsee.tech",
    "https://docker.1panel.live",
    "https://lispy.org",
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

