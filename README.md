# Docker Mirror Benchmark

🚀 自动生成的镜像源速度排行榜 (更新于 2025-06-27 03:01:10)

## 测试镜像
- 镜像名称: `library/nginx:latest`
- 测试架构: `amd64`
- 测试数据量: `10MB`

## 速度排行榜
| 排名 | 镜像源地址 | 平均下载速度 |
|------|------------|--------------|
| 1 | `docker.xuanyuan.me` | 4.40 MB/s |
| 2 | `docker.melikeme.cn` | 2.87 MB/s |
| 3 | `docker.hlmirror.com` | 2.77 MB/s |
| 4 | `lispy.org` | 2.22 MB/s |
| 5 | `docker-mirror.aigc2d.com` | 0.68 MB/s |
| 6 | `docker.kejilion.pro` | 0.17 MB/s |

## 配置

```json
{
  "registry-mirrors": [
    "https://docker.xuanyuan.me",
    "https://docker.melikeme.cn",
    "https://docker.hlmirror.com",
    "https://lispy.org",
    "https://docker-mirror.aigc2d.com"
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

