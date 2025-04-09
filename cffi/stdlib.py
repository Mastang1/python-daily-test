# 示例：调用标准 C 库的 `printf`
from cffi import FFI
ffi = FFI()

# 声明 C 函数原型
ffi.cdef("""
    int printf(const char *format, ...);
""")

# 加载 C 标准库
lib = ffi.dlopen("msvcrt")  # None 表示默认加载标准库

# 调用 C 函数
lib.printf(b"Hello, CFFI!\n")
