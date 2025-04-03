if True:
    class MyClass:
        def __init__(self):
            print("初始化 class1")
else:
    class MyClass:
        def __init__(self):
            print("初始化 class2")

if __name__ == "__main__":
    my_instance = MyClass()