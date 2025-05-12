# Docker Mirror Benchmark

🚀 自动生成的镜像源速度排行榜 (更新于 2025-05-12 23:09:20)

## 测试镜像
- 镜像名称: `library/nginx:latest`
- 测试架构: `amd64`
- 测试数据量: `10MB`

## 速度排行榜
| 排名 | 镜像源地址 | 平均下载速度 |
|------|------------|--------------|
| 1 | `docker-0.unsee.tech` | 4.44 MB/s |
| 2 | `lispy.org` | 4.00 MB/s |
| 3 | `docker.xuanyuan.me` | 3.00 MB/s |
| 4 | `docker.1panel.live` | 2.96 MB/s |
| 5 | `docker.melikeme.cn` | 2.63 MB/s |
| 6 | `a.ussh.net` | 1.81 MB/s |
| 7 | `docker.hlmirror.com` | 1.72 MB/s |
| 8 | `docker.xiaogenban1993.com` | 0.97 MB/s |
| 9 | `docker-mirror.aigc2d.com` | 0.66 MB/s |
| 10 | `docker.mybacc.com` | 0.06 MB/s |

## 配置

```json
{
  "registry-mirrors": [
    "https://docker-0.unsee.tech",
    "https://lispy.org",
    "https://docker.xuanyuan.me",
    "https://docker.1panel.live",
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

