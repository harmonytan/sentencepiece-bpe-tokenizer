# SentencePiece BPE Tokenizer

一个混合的 Python + Rust 项目，使用 `uv` 进行包管理。

## 项目结构

```
sentencepiece-bpe-tokenizer/
├── Cargo.toml          # Rust 包配置
├── pyproject.toml      # Python 包配置
├── setup.py            # 备选构建配置
├── src/
│   └── lib.rs          # Rust 源码
├── sb_tokenizer/        # Python 包
│   └── __init__.py     # Python 包入口
└── .uv/                 # uv 配置
    └── config.toml
```

## 安装和设置

### 1. 安装 uv

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. 创建虚拟环境并安装依赖

```bash
# 创建虚拟环境
uv venv

# 激活虚拟环境
source .venv/bin/activate  # Linux/macOS
# 或
.venv\Scripts\activate     # Windows

# 安装项目依赖
uv pip install -e .
```

### 3. 构建 Rust 扩展

```bash
# 使用 uv 构建
uv run python setup.py build_ext --inplace

# 或者使用 cargo
cargo build --release
```

## 使用方法

```python
from sb_tokenizer import hello, add

# 调用 Python 函数
print(hello())  # "Hello from sb-tokenizer!"

# 调用 Rust 函数
result = add(5, 3)  # 8
print(result)
```

## 开发

### 安装开发依赖

```bash
uv pip install -r requirements.txt
uv pip install pytest black mypy
```

### 运行测试

```bash
# Python 测试
uv run pytest

# Rust 测试
cargo test
```

### 代码格式化

```bash
# Python 代码格式化
uv run black .

# Rust 代码格式化
cargo fmt
```

## 构建发布

```bash
# 构建 Python 包
uv run python setup.py sdist bdist_wheel

# 构建 Rust 包
cargo build --release
```

## 注意事项

- 确保 Rust 工具链已安装
- Python 版本需要 >= 3.12
- 首次构建可能需要较长时间来编译 Rust 扩展 
