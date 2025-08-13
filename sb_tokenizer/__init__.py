try:
    from ._rust import add
    
except ImportError:
    # Fallback if Rust extension is not built
    def add(left: int, right: int) -> int:
        return left + right

def hello() -> str:
    return "Hello from sb-tokenizer!"

# Export Rust functions
__all__ = ["hello", "add"]
