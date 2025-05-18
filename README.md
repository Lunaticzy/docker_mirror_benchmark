# Docker Mirror Benchmark

🚀 自动生成的镜像源速度排行榜 (更新于 2025-05-19 03:00:26)

## 测试镜像
- 镜像名称: `library/nginx:latest`
- 测试架构: `amd64`
- 测试数据量: `10MB`

## 速度排行榜
| 排名 | 镜像源地址 | 平均下载速度 |
|------|------------|--------------|
| 1 | `docker.1panel.live` | 4.27 MB/s |
| 2 | `docker.mybacc.com` | 3.66 MB/s |
| 3 | `a.ussh.net` | 3.29 MB/s |
| 4 | `docker-0.unsee.tech` | 3.19 MB/s |
| 5 | `docker.hlmirror.com` | 2.93 MB/s |
| 6 | `docker.xiaogenban1993.com` | 2.58 MB/s |
| 7 | `docker.melikeme.cn` | 1.41 MB/s |
| 8 | `docker-mirror.aigc2d.com` | 0.67 MB/s |

## 配置

```json
{
  "registry-mirrors": [
    "https://docker.1panel.live",
    "https://docker.mybacc.com",
    "https://a.ussh.net",
    "https://docker-0.unsee.tech",
    "https://docker.hlmirror.com"
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

