import os, time
from datetime import datetime
 
def get_file_creation_time(filepath):
    return os.path.getmtime(filepath)

if __name__ == '__main__':
    testPath = os.path.dirname(os.path.abspath(__file__))
    fileTime = get_file_creation_time(testPath)
    curTime = time.time()
    difference = curTime - 1727259791.0
    print(curTime, difference)

# Flush file manager
import os
import shutil
import platform
 
# 拷贝文件的函数
def copy_file(src, dst):
    shutil.copy2(src, dst)  # 拷贝文件
    refresh_explorer(dst)  # 刷新文件管理器
 
# 刷新文件管理器的函数
def refresh_explorer(directory):
    system = platform.system()
    if system == 'Windows':
        os.system('explorer.exe ' + directory)
    elif system == 'Darwin':  # macOS
        os.system('osascript -e \'tell application "Finder" to refresh\'' )
    else:
        print("Unsupported operating system.")
 
# 示例使用
src_file = 'source.txt'
dst_directory = 'destination_directory'
 
copy_file(src_file, dst_directory)