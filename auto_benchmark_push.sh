#!/bin/bash
# 文件名: auto_benchmark_push.sh
# 描述: 自动执行基准测试并推送结果到Git仓库

# ===================== 配置区 (按需修改) =====================
REPO_DIR="/home/lunatic/works/docker_mirror_benchmark"    # Git仓库的绝对路径
PY_SCRIPT="main.py" # 要执行的Python脚本
BRANCH="main"                          # 要推送的分支
REMOTE="main"                        # 远程仓库名称
LOG_FILE="${REPO_DIR}/cron.log"        # 日志文件路径

# Git身份配置
GIT_USERNAME="Auto Committer"
GIT_EMAIL="auto@example.com"

# ===================== 函数定义 =====================
init_ssh_agent() {
    # 初始化SSH Agent (如果使用SSH认证)
    eval "$(ssh-agent -s)"
    ssh-add ~/.ssh/github  # 你的SSH私钥路径
}

check_errors() {
    # 检查上一条命令的退出状态
    if [ $? -ne 0 ]; then
        echo "[ERROR] 步骤失败: $1"
        exit 1
    fi
}

# ===================== 主逻辑 =====================
{
    echo "====== 任务开始: $(date +'%Y-%m-%d %H:%M:%S') ======"

    # 进入工作目录
    cd "$REPO_DIR" || exit 1
    echo "工作目录: $(pwd)"

    # 初始化环境 (SSH示例，如用HTTPS可删除)
    init_ssh_agent

    # 拉取最新代码
    echo "正在同步远程仓库..."
    git fetch "$REMOTE"
    git reset --hard "$REMOTE/$BRANCH"
    check_errors "拉取代码失败"

    # 执行基准测试
    echo "正在执行基准测试..."
    /home/lunatic/.local/bin/uv run "$PY_SCRIPT"
    check_errors "基准测试执行失败"

    # 检查文件变更
    if git diff-index --quiet HEAD --; then
        echo "没有检测到文件变更"
        exit 0
    fi

    # 提交变更
    echo "检测到文件变更，正在提交..."
    git add README.md daemon.json
    git -c user.name="$GIT_USERNAME" \
        -c user.email="$GIT_EMAIL" \
        commit -m "📊 自动更新: $(date +'%Y-%m-%d %H:%M:%S')"
    check_errors "提交失败"

    # 推送变更
    echo "正在推送变更到 $REMOTE/$BRANCH ..."
    git push "$REMOTE" "$BRANCH" 2>&1
    check_errors "推送失败"

    echo "====== 任务完成 ======"
} >> "$LOG_FILE" 2>&1