from setuptools import setup, find_packages
from setuptools_rust import RustExtension

setup(
    name="sb-tokenizer",
    version="0.1.0",
    packages=find_packages(),
    rust_extensions=[
        RustExtension("sb_tokenizer._rust", "src/lib.rs")
    ],
    install_requires=[],
    python_requires=">=3.12",
)
