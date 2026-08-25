# Claude Code

Claude Code discovers project Skills from `.claude/skills/`. Link or copy the
first-party Skill directories into that location:

```bash
mkdir -p .claude/skills
ln -s /path/to/ta-skills/digitize-math-lectures .claude/skills/digitize-math-lectures
ln -s /path/to/ta-skills/math-exposition-latex .claude/skills/math-exposition-latex
ln -s /path/to/ta-skills/tsqx-gen .claude/skills/tsqx-gen
```

For the Anthropic `math-olympiad` vendor Skill, prefer installing the upstream
official plugin directly rather than treating this repository as its source.
