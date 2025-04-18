# ... existing code ...
ffi.cdef("""
    int add(int a, int b);
""")

# 关键修改：交叉编译支持
ffi.set_source("_embedded_example", r"""
    int add(int a, int b) { 
        return a + b; 
    }
""", libraries=[], target="arm-linux-gnueabihf")  # 指定交叉编译工具链

ffi.compile()  # 在宿主机交叉编译后部署到嵌入式设备
