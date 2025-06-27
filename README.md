# Docker Mirror Benchmark

🚀 自动生成的镜像源速度排行榜 (更新于 2025-06-28 03:00:33)

## 测试镜像
- 镜像名称: `library/nginx:latest`
- 测试架构: `amd64`
- 测试数据量: `10MB`

## 速度排行榜
| 排名 | 镜像源地址 | 平均下载速度 |
|------|------------|--------------|
| 1 | `docker.hlmirror.com` | 4.32 MB/s |
| 2 | `docker.xuanyuan.me` | 3.33 MB/s |
| 3 | `docker.melikeme.cn` | 2.49 MB/s |
| 4 | `docker-0.unsee.tech` | 2.48 MB/s |
| 5 | `lispy.org` | 1.16 MB/s |

## 配置

```json
{
  "registry-mirrors": [
    "https://docker.hlmirror.com",
    "https://docker.xuanyuan.me",
    "https://docker.melikeme.cn",
    "https://docker-0.unsee.tech",
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

