try:
    from ._rust import *
except ImportError as e:
    # Fallback if Rust module is not available
    print(f"Warning: Could not import Rust module: {e}")
    pass

def hello() -> str:
    return "Hello from sb-tokenizer!"

__version__ = "0.1.0"
