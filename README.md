# Docker Mirror Benchmark

🚀 自动生成的镜像源速度排行榜 (更新于 2025-06-02 03:00:31)

## 测试镜像
- 镜像名称: `library/nginx:latest`
- 测试架构: `amd64`
- 测试数据量: `10MB`

## 速度排行榜
| 排名 | 镜像源地址 | 平均下载速度 |
|------|------------|--------------|
| 1 | `docker.melikeme.cn` | 2.55 MB/s |
| 2 | `lispy.org` | 1.43 MB/s |
| 3 | `a.ussh.net` | 0.68 MB/s |
| 4 | `docker-mirror.aigc2d.com` | 0.64 MB/s |
| 5 | `docker.xuanyuan.me` | 0.64 MB/s |

## 配置

```json
{
  "registry-mirrors": [
    "https://docker.melikeme.cn",
    "https://lispy.org",
    "https://a.ussh.net",
    "https://docker-mirror.aigc2d.com",
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

