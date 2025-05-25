# Docker Mirror Benchmark

🚀 自动生成的镜像源速度排行榜 (更新于 2025-05-26 03:00:25)

## 测试镜像
- 镜像名称: `library/nginx:latest`
- 测试架构: `amd64`
- 测试数据量: `10MB`

## 速度排行榜
| 排名 | 镜像源地址 | 平均下载速度 |
|------|------------|--------------|
| 1 | `docker-0.unsee.tech` | 4.15 MB/s |
| 2 | `lispy.org` | 3.84 MB/s |
| 3 | `docker.xiaogenban1993.com` | 2.43 MB/s |
| 4 | `docker.melikeme.cn` | 2.37 MB/s |
| 5 | `docker.xuanyuan.me` | 2.05 MB/s |
| 6 | `a.ussh.net` | 1.94 MB/s |
| 7 | `docker.mybacc.com` | 1.81 MB/s |
| 8 | `docker.hlmirror.com` | 1.36 MB/s |
| 9 | `docker-mirror.aigc2d.com` | 0.74 MB/s |

## 配置

```json
{
  "registry-mirrors": [
    "https://docker-0.unsee.tech",
    "https://lispy.org",
    "https://docker.xiaogenban1993.com",
    "https://docker.melikeme.cn",
    "https://docker.xuanyuan.me"
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

