import os
path1 = "D:\\workspace\\test_python\\python-daily-test"
path2 = "D:\\workspace\\test_python\\python-daily-test"
are_same = os.path.samefile(path1, path2)
print(are_same)  # 如果路径相同输出True，否则输出False
