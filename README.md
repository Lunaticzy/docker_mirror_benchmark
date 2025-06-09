# Docker Mirror Benchmark

🚀 自动生成的镜像源速度排行榜 (更新于 2025-06-10 03:04:08)

## 测试镜像
- 镜像名称: `library/nginx:latest`
- 测试架构: `amd64`
- 测试数据量: `10MB`

## 速度排行榜
| 排名 | 镜像源地址 | 平均下载速度 |
|------|------------|--------------|
| 1 | `docker.hlmirror.com` | 4.00 MB/s |
| 2 | `lispy.org` | 3.37 MB/s |
| 3 | `docker.melikeme.cn` | 3.33 MB/s |
| 4 | `a.ussh.net` | 3.07 MB/s |
| 5 | `docker.xuanyuan.me` | 2.98 MB/s |
| 6 | `docker-0.unsee.tech` | 2.93 MB/s |
| 7 | `docker.kejilion.pro` | 0.04 MB/s |

## 配置

```json
{
  "registry-mirrors": [
    "https://docker.hlmirror.com",
    "https://lispy.org",
    "https://docker.melikeme.cn",
    "https://a.ussh.net",
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

