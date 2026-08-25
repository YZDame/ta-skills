# Mistral OCR

这是 `ta-skills` 中的 Mistral OCR Skill。它使用 Mistral 官方 OCR API，把 PDF、扫描页、图片或公开文档 URL 转成 Markdown 和原始 JSON。

## 配置

脚本只从环境变量 `MISTRAL_API_KEY` 读取密钥，不接受命令行密钥，也不应把真实密钥写入仓库：

```bash
export MISTRAL_API_KEY='your-key'
python3 scripts/mistral_ocr.py input.pdf
```

本地 PDF 和图片默认会上传到 Mistral 服务。需要本地-only 处理时，应改用其他 OCR 工具；`--no-upload` 会明确拒绝本地文件上传。

## 输出

脚本默认生成：

- `content.md`：按页排列的 Markdown
- `response.json`：原始 OCR 响应，包括页面、表格、图像、区块和用量信息（如果 API 返回）

OCR 结果是中间材料。数学公式、表格、图形和页序仍需人工检查。

官方参考：

- <https://docs.mistral.ai/studio-api/document-processing/basic_ocr>
- <https://docs.mistral.ai/api/endpoint/ocr>
