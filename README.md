# Docker Mirror Benchmark

🚀 自动生成的镜像源速度排行榜 (更新于 2025-05-24 03:00:42)

## 测试镜像
- 镜像名称: `library/nginx:latest`
- 测试架构: `amd64`
- 测试数据量: `10MB`

## 速度排行榜
| 排名 | 镜像源地址 | 平均下载速度 |
|------|------------|--------------|
| 1 | `lispy.org` | 4.47 MB/s |
| 2 | `docker.melikeme.cn` | 3.84 MB/s |
| 3 | `docker.xuanyuan.me` | 3.06 MB/s |
| 4 | `docker-0.unsee.tech` | 2.71 MB/s |
| 5 | `docker.mybacc.com` | 2.66 MB/s |
| 6 | `a.ussh.net` | 2.00 MB/s |
| 7 | `docker.xiaogenban1993.com` | 1.18 MB/s |
| 8 | `docker-mirror.aigc2d.com` | 0.65 MB/s |
| 9 | `docker.hlmirror.com` | 0.35 MB/s |

## 配置

```json
{
  "registry-mirrors": [
    "https://lispy.org",
    "https://docker.melikeme.cn",
    "https://docker.xuanyuan.me",
    "https://docker-0.unsee.tech",
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

