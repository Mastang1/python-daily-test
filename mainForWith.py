class WithTest:
    def __init__(self):
        print("Init")
       

    def __enter__(self):
        print("Entry".center(9, "*"))
    """
    exception: 异常
    exception_type : 异常类型
    exception_value : 异常的值（原因）
    exception_traceback : 异常发生的位置（回溯、追溯）
    """
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("异常类型：", exc_type)
        print("异常的值：", exc_val)
        print("异常发生的位置：", exc_tb)
        print("Exit".center(50, "*"))


with WithTest() as w:
    print("运行前".center(50, "*"))
    20/0
    print("运行后".center(50, "*"))
