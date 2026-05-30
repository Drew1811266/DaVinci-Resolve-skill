# DaVinci Resolve Skill

这是一个平台无关的 AI Agent Skill，用于帮助 Agent 规划、引导、编写脚本并验证 DaVinci Resolve 工作流。

它面向需要让 AI 协助操作 DaVinci Resolve 的场景，覆盖素材导入、项目创建、时间线管理、剪辑、字幕、Fusion、调色、Fairlight 音频、渲染、批量导出、故障排查和项目安全等任务。

## 这个 Skill 能做什么

这个 Skill 可以帮助 AI Agent：

- 理解用户提出的 DaVinci Resolve 操作目标。
- 在 UI 指导、脚本自动化、混合流程、UI 自动化或暂停确认之间选择合适的执行方式。
- 避免对 Resolve 版本、Free/Studio 授权版本、操作系统、编码器、菜单、快捷键和脚本 API 做危险假设。
- 使用 Action Cards 把常见任务转换成标准化流程。
- 在删除、覆盖、重链、批量修改等高风险操作前要求用户明确确认。
- 为每个操作计划提供验证步骤和回滚建议。

这个 Skill 不是让 Agent 声称自己知道所有 Resolve 命令或 API。相反，它要求 Agent 对版本相关、授权相关和 API 相关的信息进行验证，优先依据已安装的 Developer 文档、Blackmagic Design 官方文档，或用户提供的权威上下文。

## 仓库结构

```text
davinci-resolve/
  SKILL.md                       AI Agent 的运行时入口
  manifest.yaml                  平台无关的 Skill 元数据
  agents/openai.yaml             可选的 OpenAI/Codex UI 元数据
  action_cards/                  常见任务的机器可读工作流
  references/                    可复用策略、schema、模板和示例
  sources/                       知识来源注册表和版本矩阵模板
  evals/                         安全与幻觉检查测试任务
  scripts/                       校验工具
```

## 运行时入口

Agent 应先读取 `SKILL.md`。它包含这个 Skill 的核心行为规则：

- 先解析任务，再选择执行模式。
- 只询问真正影响执行和风险判断的缺失信息。
- 在破坏性操作或大范围修改前要求用户明确确认。
- 不编造菜单、快捷键、API 方法、文件路径、编码器或版本专属功能。
- 输出验证方式和回滚建议。

其他支持文件只在需要时加载。

## Action Cards

`action_cards/` 中包含常见 Resolve 操作的 YAML 任务卡片，例如：

- 导入素材文件夹。
- 创建项目。
- 基于素材创建时间线。
- 导出时间线 XML。
- 添加渲染任务。
- 批量导出时间线。
- 创建或导入字幕。
- 音频响度标准化。
- 应用 LUT。
- 创建 Fusion 标题。
- 备份项目。

每张卡片都定义了必需输入、执行前检查、可用执行模式、安全门槛、通用步骤、验证方式和回滚建议。

## 安全模型

除非经过明确确认，否则 Skill 会把以下行为视为高风险：

- 删除素材、bin、时间线或渲染文件。
- 重链素材。
- 覆盖渲染输出。
- 批量修改剪辑。
- 修改项目或时间线帧率。
- 修改色彩管理。
- 启动大型批量渲染。
- 修改协作项目。

Agent 必须在这些操作前要求用户明确确认，并应在大范围修改前建议备份。

## 脚本策略

只有在官方文档、已安装的 Developer 文档或用户提供的权威资料确认所需 API 对象和方法后，Agent 才应生成可执行的 Resolve 自动化脚本。

如果 API 支持不确定，Agent 应提供伪代码和需要验证的 API 清单，而不是编造方法名。

相关文件：

- `references/scripting_policy.md`
- `references/scripting/examples/connect_to_resolve.py`

## 校验

运行资产校验：

```bash
python3 scripts/validate_skill_assets.py
```

如果使用 Codex 的 `skill-creator` 工具，也可以运行：

```bash
python3 /path/to/skill-creator/scripts/quick_validate.py .
```

## 可迁移性

核心内容使用 Markdown、YAML 和 Python 示例表达，便于迁移到不同 AI 平台。平台专属元数据应隔离在 `agents/` 或其他适配层目录中，不应写入核心运行逻辑。
