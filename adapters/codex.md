# Codex

Codex discovers project Skills from `.agents/skills/`. From a checked-out copy
of this repository, link the first-party directories into the project that
will use them:

```bash
mkdir -p .agents/skills
ln -s /path/to/ta-skills/digitize-math-lectures .agents/skills/digitize-math-lectures
ln -s /path/to/ta-skills/math-exposition-latex .agents/skills/math-exposition-latex
ln -s /path/to/ta-skills/tsqx-gen .agents/skills/tsqx-gen
```

The vendor Skills are optional and should be linked separately when their
upstream terms permit local use.
