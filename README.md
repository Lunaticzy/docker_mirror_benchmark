# Docker Mirror Benchmark

🚀 自动生成的镜像源速度排行榜 (更新于 2025-09-01 03:00:12)

## 测试镜像
- 镜像名称: `library/nginx:latest`
- 测试架构: `amd64`
- 测试数据量: `10MB`

## 速度排行榜
⚠️ 当前没有可用的镜像源数据

## 配置

```json
{
  "registry-mirrors": [],
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

