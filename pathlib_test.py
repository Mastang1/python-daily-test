from pathlib import Path
import re

# 指定目标路径（替换为实际路径）
target_path = Path(r"C:\tangyapeng\repos\type_py\python-daily-test\tftpy-test")

# 确保路径存在
if not target_path.exists():
    print(f"路径不存在: {target_path}")
else:
    # 筛选一级目录下的文件（排除文件夹）
    file_list = [entry.name for entry in target_path.iterdir() if entry.is_dir()]
    
    # 打印结果
    print(f"指定路径下的一级文件列表: {target_path}")
    for file in file_list:
        print(f"- {file}")