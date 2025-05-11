# Docker Mirror Benchmark

🚀 自动生成的镜像源速度排行榜 (更新于 2025-05-11 19:49:37)

## 测试镜像
- 镜像名称: `library/nginx:latest`
- 测试架构: `amd64`
- 测试数据量: `10MB`

## 速度排行榜
| 排名 | 镜像源地址 | 平均下载速度 |
|------|------------|--------------|
| 1 | `lispy.org` | 4.53 MB/s |
| 2 | `a.ussh.net` | 4.52 MB/s |
| 3 | `docker.1panel.live` | 3.74 MB/s |
| 4 | `docker.hlmirror.com` | 3.04 MB/s |
| 5 | `docker.xiaogenban1993.com` | 2.34 MB/s |
| 6 | `docker.xuanyuan.me` | 2.14 MB/s |
| 7 | `docker.mybacc.com` | 1.90 MB/s |
| 8 | `docker.melikeme.cn` | 1.82 MB/s |
| 9 | `docker-0.unsee.tech` | 1.55 MB/s |
| 10 | `docker-mirror.aigc2d.com` | 0.71 MB/s |

## 配置

```json
{
  "registry-mirrors": [
    "https://lispy.org",
    "https://a.ussh.net",
    "https://docker.1panel.live",
    "https://docker.hlmirror.com",
    "https://docker.xiaogenban1993.com"
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

