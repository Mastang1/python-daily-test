import os, sys

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def __repr__(self):
        return f"Circle({self.center}, r={self.radius})"

# 创建一个Circle对象
c = Circle((0, 0), 5)

# 使用repr()函数获取对象的字符串表示
repr_c = repr(c)
print(repr_c)  # 输出: Circle((0, 0), r=5)

# 在交互式解释器中直接输入对象
# 这将调用__repr__方法并显示返回的字符串
#c
# 输出: Circle((0, 0), r=5)

# 使用eval()函数和__repr__返回的字符串重新创建对象
# 注意：这仅适用于返回有效Python表达式的__repr__实现
c2 = eval(repr_c)
print(c2)  # 输出: Circle((0, 0), r=5)
