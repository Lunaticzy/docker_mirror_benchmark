# Docker Mirror Benchmark

🚀 自动生成的镜像源速度排行榜 (更新于 2025-05-21 03:00:31)

## 测试镜像
- 镜像名称: `library/nginx:latest`
- 测试架构: `amd64`
- 测试数据量: `10MB`

## 速度排行榜
| 排名 | 镜像源地址 | 平均下载速度 |
|------|------------|--------------|
| 1 | `docker.1panel.live` | 5.01 MB/s |
| 2 | `docker.hlmirror.com` | 4.90 MB/s |
| 3 | `lispy.org` | 4.81 MB/s |
| 4 | `docker-0.unsee.tech` | 3.81 MB/s |
| 5 | `docker.melikeme.cn` | 3.27 MB/s |
| 6 | `docker.xuanyuan.me` | 3.16 MB/s |
| 7 | `a.ussh.net` | 2.48 MB/s |
| 8 | `docker.xiaogenban1993.com` | 2.09 MB/s |
| 9 | `docker.mybacc.com` | 2.05 MB/s |
| 10 | `docker-mirror.aigc2d.com` | 0.58 MB/s |

## 配置

```json
{
  "registry-mirrors": [
    "https://docker.1panel.live",
    "https://docker.hlmirror.com",
    "https://lispy.org",
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

