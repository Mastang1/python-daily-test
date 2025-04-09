from cffi import FFI
ffi = FFI()

# 定义 C 代码
ffi.set_source("_example", """
    int add(int a, int b) {
        return a + b;
    }
""")

# 声明函数接口
ffi.cdef("""
    int add(int a, int b);
""")

# 编译并加载
ffi.compile()
from _example import lib

# 调用 C 函数
print(lib.add(3, 5))  # 输出 8
