import subprocess

# 使用 shell 执行 Windows 内置命令
result = subprocess.run(
    'dir',  # 直接作为字符串传入命令
    shell=True,  # 使用 shell 执行
    capture_output=True,
    text=True
)

# 打印结果
if result.returncode == 0:
    print("命令成功执行，输出如下：")
    print(result.stdout)
else:
    print("命令执行失败，错误如下：")
    print(result.stderr)
