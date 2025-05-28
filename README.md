# Docker Mirror Benchmark

🚀 自动生成的镜像源速度排行榜 (更新于 2025-05-29 03:00:25)

## 测试镜像
- 镜像名称: `library/nginx:latest`
- 测试架构: `amd64`
- 测试数据量: `10MB`

## 速度排行榜
| 排名 | 镜像源地址 | 平均下载速度 |
|------|------------|--------------|
| 1 | `docker.xuanyuan.me` | 4.53 MB/s |
| 2 | `docker.hlmirror.com` | 4.48 MB/s |
| 3 | `lispy.org` | 4.43 MB/s |
| 4 | `docker.melikeme.cn` | 3.84 MB/s |
| 5 | `docker-0.unsee.tech` | 3.72 MB/s |
| 6 | `a.ussh.net` | 3.02 MB/s |
| 7 | `docker-mirror.aigc2d.com` | 0.75 MB/s |

## 配置

```json
{
  "registry-mirrors": [
    "https://docker.xuanyuan.me",
    "https://docker.hlmirror.com",
    "https://lispy.org",
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

