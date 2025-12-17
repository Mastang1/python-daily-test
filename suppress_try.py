from contextlib import suppress

# 1. 最常见：只吞特定异常（强烈推荐）
with suppress(FileNotFoundError):
    os.remove("tmp.log")

with suppress(KeyError, IndexError, AttributeError):
    value = config["database"]["password"]

# 2. Python 3.11+ 新语法：什么都不写 = 吞所有异常
with suppress():                     # 等价于 suppress(Exception)
    risky()

# 3. 多段代码连着吞（超级好看）
with suppress(FileNotFoundError), suppress(PermissionError):
    os.remove("important.txt")

# 删除文件时不在乎是否存在
with suppress(FileNotFoundError):
    os.remove("cache.db")

# 解析可能不标准的 JSON
with suppress(json.JSONDecodeError):
    data = json.loads(user_input)

# 字典取值永远不炸
with suppress(KeyError):
    os.environ.pop("HTTP_X_API_KEY", None)

# 清理资源时不在乎失败
with suppress(OSError):
    shutil.rmtree("temp_dir")
    os.kill(pid, 9)
    socket.close()