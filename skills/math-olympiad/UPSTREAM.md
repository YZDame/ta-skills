# `math-olympiad` 上游来源

- 上游作者：Anthropic
- 上游仓库：<https://github.com/anthropics/claude-plugins-official>
- 上游插件目录：<https://github.com/anthropics/claude-plugins-official/tree/main/plugins/math-olympiad>
- 本仓库引入的固定版本：[`b819188d2eea14e0400556ca29dbd1179a7c595b`](https://github.com/anthropics/claude-plugins-official/tree/b819188d2eea14e0400556ca29dbd1179a7c595b/plugins/math-olympiad)
- 引入路径：`plugins/math-olympiad/skills/math-olympiad`
- 许可证：Apache License 2.0，全文见本目录 [`LICENSE`](LICENSE)

## 本仓库所作修改

`SKILL.md` 删除了上游前置字段 `version: 0.1.0`，因为当前 Agent Skills 校验只接受 `name` 和 `description`。修改位置保留了显著说明，其余 Skill 文件与上述固定版本一致。

上游 `math-olympiad` 插件目录在该固定版本中没有 `NOTICE` 文件。

## 再发布要求

再发布或继续修改这些文件时，应保留 Apache License 2.0 全文、Anthropic 上游链接、已有署名以及修改说明。根目录的 `ta-skills` 许可证不会替代这些要求。
