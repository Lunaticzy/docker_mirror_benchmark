# Docker Mirror Benchmark

🚀 自动生成的镜像源速度排行榜 (更新于 2025-05-15 03:00:26)

## 测试镜像
- 镜像名称: `library/nginx:latest`
- 测试架构: `amd64`
- 测试数据量: `10MB`

## 速度排行榜
| 排名 | 镜像源地址 | 平均下载速度 |
|------|------------|--------------|
| 1 | `docker.1panel.live` | 5.84 MB/s |
| 2 | `lispy.org` | 4.85 MB/s |
| 3 | `docker.xiaogenban1993.com` | 4.48 MB/s |
| 4 | `docker.melikeme.cn` | 3.90 MB/s |
| 5 | `docker-0.unsee.tech` | 3.14 MB/s |
| 6 | `docker.xuanyuan.me` | 2.87 MB/s |
| 7 | `docker.mybacc.com` | 2.65 MB/s |
| 8 | `a.ussh.net` | 2.07 MB/s |
| 9 | `docker.hlmirror.com` | 1.63 MB/s |
| 10 | `docker-mirror.aigc2d.com` | 0.65 MB/s |

## 配置

```json
{
  "registry-mirrors": [
    "https://docker.1panel.live",
    "https://lispy.org",
    "https://docker.xiaogenban1993.com",
    "https://docker.melikeme.cn",
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

