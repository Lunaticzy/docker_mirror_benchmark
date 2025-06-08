# Docker Mirror Benchmark

🚀 自动生成的镜像源速度排行榜 (更新于 2025-06-09 03:00:30)

## 测试镜像
- 镜像名称: `library/nginx:latest`
- 测试架构: `amd64`
- 测试数据量: `10MB`

## 速度排行榜
| 排名 | 镜像源地址 | 平均下载速度 |
|------|------------|--------------|
| 1 | `docker-0.unsee.tech` | 4.50 MB/s |
| 2 | `lispy.org` | 1.85 MB/s |
| 3 | `docker.xuanyuan.me` | 1.62 MB/s |
| 4 | `docker.melikeme.cn` | 1.20 MB/s |
| 5 | `a.ussh.net` | 1.04 MB/s |
| 6 | `docker.hlmirror.com` | 1.03 MB/s |
| 7 | `docker-mirror.aigc2d.com` | 0.54 MB/s |

## 配置

```json
{
  "registry-mirrors": [
    "https://docker-0.unsee.tech",
    "https://lispy.org",
    "https://docker.xuanyuan.me",
    "https://docker.melikeme.cn",
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

