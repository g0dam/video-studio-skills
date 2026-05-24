# Example Taste Profiles

This directory contains sample taste profiles that demonstrate the expected file shape:

```text
examples/taste/<taste-slug>/
  manifest.json
  taste.md
  source-log.md
  prompt-vocabulary.md
```

Validate the examples with:

```bash
python3 scripts/validate_taste.py examples/taste
```

Keep your active project taste profiles in the root `taste/` directory or in your own project workspace. The examples are for reference only.

---

# 示例 Taste Profile

这里放的是示例 taste profile，用来展示标准文件结构：

```text
examples/taste/<taste-slug>/
  manifest.json
  taste.md
  source-log.md
  prompt-vocabulary.md
```

可以用下面的命令校验：

```bash
python3 scripts/validate_taste.py examples/taste
```

真实项目的 taste profile 建议放在根目录 `taste/`，或放在你自己的项目工作区里。这里的 examples 只作为参考。
