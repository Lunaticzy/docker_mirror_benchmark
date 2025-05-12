# Docker Mirror Benchmark

🚀 自动生成的镜像源速度排行榜 (更新于 2025-05-13 03:00:27)

## 测试镜像
- 镜像名称: `library/nginx:latest`
- 测试架构: `amd64`
- 测试数据量: `10MB`

## 速度排行榜
| 排名 | 镜像源地址 | 平均下载速度 |
|------|------------|--------------|
| 1 | `docker.xiaogenban1993.com` | 4.90 MB/s |
| 2 | `docker.1panel.live` | 4.46 MB/s |
| 3 | `a.ussh.net` | 4.39 MB/s |
| 4 | `docker-0.unsee.tech` | 4.05 MB/s |
| 5 | `lispy.org` | 3.60 MB/s |
| 6 | `docker.xuanyuan.me` | 3.12 MB/s |
| 7 | `docker.hlmirror.com` | 2.65 MB/s |
| 8 | `docker.mybacc.com` | 2.07 MB/s |
| 9 | `docker.melikeme.cn` | 1.24 MB/s |
| 10 | `docker-mirror.aigc2d.com` | 0.61 MB/s |

## 配置

```json
{
  "registry-mirrors": [
    "https://docker.xiaogenban1993.com",
    "https://docker.1panel.live",
    "https://a.ussh.net",
    "https://docker-0.unsee.tech",
    "https://lispy.org"
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

