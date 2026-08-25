# DeepSeek Harness

DeepSeek Harness 只要按 Agent Skills 规范读取 `SKILL.md`，就可以直接使用本仓库的第一方 Skill。建议把每个 Skill 作为独立目录挂载，而不是把整个仓库内容拼接成一段超长系统提示词：

```text
ta-skills/
├── digitize-math-lectures/
├── math-exposition-latex/
├── tsqx-gen/
└── mistral-ocr/
```

如果 Harness 使用统一的 Skills 根目录，把上面的目录复制或链接到该目录即可。`agents/openai.yaml` 是 Codex 侧的展示元数据，不是所有 Harness 都会读取；真正的跨平台核心是 `SKILL.md` 及其相对路径下的资源。

外部脚本、OCR API、LaTeX、TSQX 和 Asymptote 依赖需要按 Harness 的权限模型单独配置。不要因为 Skill 文件可读取，就默认 Harness 有权访问本地文件、执行 shell 或上传文档。
