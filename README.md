# Docker Mirror Benchmark

🚀 自动生成的镜像源速度排行榜 (更新于 2025-05-22 03:00:58)

## 测试镜像
- 镜像名称: `library/nginx:latest`
- 测试架构: `amd64`
- 测试数据量: `10MB`

## 速度排行榜
| 排名 | 镜像源地址 | 平均下载速度 |
|------|------------|--------------|
| 1 | `docker.1panel.live` | 5.35 MB/s |
| 2 | `a.ussh.net` | 4.51 MB/s |
| 3 | `lispy.org` | 4.48 MB/s |
| 4 | `docker-0.unsee.tech` | 4.12 MB/s |
| 5 | `docker.mybacc.com` | 4.06 MB/s |
| 6 | `docker.melikeme.cn` | 3.83 MB/s |
| 7 | `docker.hlmirror.com` | 3.66 MB/s |
| 8 | `docker.xiaogenban1993.com` | 3.46 MB/s |
| 9 | `docker.xuanyuan.me` | 2.73 MB/s |

## 配置

```json
{
  "registry-mirrors": [
    "https://docker.1panel.live",
    "https://a.ussh.net",
    "https://lispy.org",
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

