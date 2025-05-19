# Docker Mirror Benchmark

🚀 自动生成的镜像源速度排行榜 (更新于 2025-05-20 03:00:29)

## 测试镜像
- 镜像名称: `library/nginx:latest`
- 测试架构: `amd64`
- 测试数据量: `10MB`

## 速度排行榜
| 排名 | 镜像源地址 | 平均下载速度 |
|------|------------|--------------|
| 1 | `docker.1panel.live` | 5.00 MB/s |
| 2 | `docker-0.unsee.tech` | 4.77 MB/s |
| 3 | `docker.mybacc.com` | 4.51 MB/s |
| 4 | `docker.xuanyuan.me` | 1.97 MB/s |
| 5 | `lispy.org` | 1.56 MB/s |
| 6 | `docker.hlmirror.com` | 1.53 MB/s |
| 7 | `docker-mirror.aigc2d.com` | 0.59 MB/s |

## 配置

```json
{
  "registry-mirrors": [
    "https://docker.1panel.live",
    "https://docker-0.unsee.tech",
    "https://docker.mybacc.com",
    "https://docker.xuanyuan.me",
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

