# LLM-ROS2-Navigation-Agenta
## 项目简介

本项目面向移动机器人自然语言任务执行场景，用户可以输入“先去门口，再到桌子旁，最后返回充电点”等中文指令。
系统计划利用大语言模型将自然语言解析为结构化任务，并通过 ROS2 与 Nav2 控制 TurtleBot3 在仿真环境中完成单点或多目标自主导航。

项目计划加入地点校验、任务状态反馈和异常处理，用于提升大模型指令执行的可靠性。该项目将大模型应用、ROS2 软件开发和机器人导航结合起来，能够体现完整的智能机器人系统开发能力。
## 当前状态

V0.1：正在建立项目仓库和开发环境。

目前尚未实现大模型解析、ROS2 节点和 Nav2 导航。
## 开发环境

- Ubuntu 22.04
- ROS2 Humble
- Python 3.10
## 安装

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
```

## 运行

```bash
llm-nav-agent
```

预期输出：

```text
LLM-ROS2-Navigation-Agent: V0.1 environment ready
```

## 测试

```bash
python -m unittest discover -s tests -v
```

## 当前限制

- 尚未接入大语言模型 API。
- 尚未实现 ROS2 节点通信。
- 尚未连接 Nav2 执行导航。
- 当前版本只验证 Python 项目结构、安装流程和测试流程。

## License

本项目使用 [MIT License](LICENSE)。
