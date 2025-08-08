# Docker Mirror Benchmark

🚀 自动生成的镜像源速度排行榜 (更新于 2025-08-09 03:00:35)

## 测试镜像
- 镜像名称: `library/nginx:latest`
- 测试架构: `amd64`
- 测试数据量: `10MB`

## 速度排行榜
| 排名 | 镜像源地址 | 平均下载速度 |
|------|------------|--------------|
| 1 | `docker.367231.xyz` | 2.54 MB/s |
| 2 | `lispy.org` | 0.97 MB/s |

## 配置

```json
{
  "registry-mirrors": [
    "https://docker.367231.xyz",
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

