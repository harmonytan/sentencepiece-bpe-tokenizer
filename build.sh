#!/bin/bash

# 构建 Rust 扩展并安装到 Python 环境
echo "🔨 构建 Rust 扩展..."
uv run maturin develop

echo "✅ 构建完成！"
echo "现在你可以运行: python -c \"from sb_tokenizer import hello, add; print(hello()); print(add(5, 3))\""
