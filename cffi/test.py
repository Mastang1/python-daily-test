from cffi import FFI
import math

# 初始化FFI
ffi = FFI()

# 声明C接口（类似.h文件）
ffi.cdef("""
    // 基本类型
    int Add(int a, int b);

    // 字符串
    const char* ReverseString(char* str);

    // 结构体
    typedef struct {
        int x;
        float y;
    } Point;
    float PointDistance(Point p1, Point p2);

    // 回调函数
    typedef int (*Callback)(int);
    void ProcessNumbers(int* arr, int size, Callback cb);
""")

p = ffi.new("Point*", {'x': 1, 'y': 2.0})  # 结构体
s = ffi.new("char[]", b"hello")  # 字符串
arr = ffi.new("int[]", [1, 2, 3])  # 数组
print(type(arr))