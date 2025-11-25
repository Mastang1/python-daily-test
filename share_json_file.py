import json
import os
import time
import random
import tempfile

# 简单的共享文件夹JSON读写方案
# 使用临时文件+重命名保证原子性，避免读写冲突

def read_json_safe(file_path, max_retries=10, retry_delay=0.1):
    """
    安全读取JSON文件，避免写入冲突
    """
    for i in range(max_retries):
        try:
            # 尝试直接读取
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            # 文件不存在或格式错误，返回None
            return None
        except (IOError, PermissionError) as e:
            # 文件可能正在被写入，等待后重试
            if i < max_retries - 1:
                time.sleep(retry_delay * (i + 1))
                continue
            raise e
    return None

def write_json_safe(file_path, data, max_retries=10, retry_delay=0.1):
    """
    安全写入JSON文件，使用临时文件+重命名保证原子性
    """
    # 创建临时文件
    dir_path = os.path.dirname(file_path)
    with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', 
                                   dir=dir_path, 
                                   delete=False,
                                   suffix='.tmp') as temp_file:
        temp_path = temp_file.name
        json.dump(data, temp_file, ensure_ascii=False, indent=2)
    
    # 尝试重命名临时文件为目标文件（原子操作）
    for i in range(max_retries):
        try:
            # Windows下可能需要先删除目标文件
            if os.path.exists(file_path):
                os.remove(file_path)
            os.rename(temp_path, file_path)
            return True
        except (IOError, PermissionError) as e:
            # 文件可能正在被读取，等待后重试
            if i < max_retries - 1:
                time.sleep(retry_delay * (i + 1))
                continue
            # 重试失败，删除临时文件
            try:
                os.remove(temp_path)
            except:
                pass
            raise e
    return False

# 示例使用
if __name__ == "__main__":
    # 共享文件夹路径
    shared_folder = "C:/shared_folder"  # 替换为你的共享文件夹路径
    json_file = os.path.join(shared_folder, "data.json")
    
    # 确保共享文件夹存在
    os.makedirs(shared_folder, exist_ok=True)
    
    # 写入数据
    data_to_write = {
        "message": "Hello from OS1",
        "timestamp": time.time(),
        "data": [1, 2, 3, 4, 5]
    }
    
    print("写入数据...")
    write_json_safe(json_file, data_to_write)
    print("写入完成")
    
    # 读取数据
    print("读取数据...")
    data_read = read_json_safe(json_file)
    if data_read:
        print("读取成功:", data_read)
    else:
        print("读取失败或文件不存在")
