#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试文件夹监控程序
"""

import os
import sys
import time
import subprocess
import threading
import tempfile
import shutil


def run_monitor(monitor_script, folder_path):
    """运行监控脚本并捕获输出"""
    print(f"启动监控进程，监控文件夹: {folder_path}")
    # 使用subprocess.Popen启动监控脚本
    process = subprocess.Popen(
        [sys.executable, monitor_script, folder_path],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1,
        universal_newlines=True
    )
    
    # 等待监控程序启动
    time.sleep(2)
    
    return process


def test_file_operations(folder_path):
    """在监控文件夹中执行文件操作"""
    print("\n开始文件操作测试...")
    
    # 1. 创建文件
    test_file = os.path.join(folder_path, "test1.txt")
    with open(test_file, 'w', encoding='utf-8') as f:
        f.write("这是一个测试文件")
    print(f"创建文件: {test_file}")
    time.sleep(0.5)
    
    # 2. 修改文件
    with open(test_file, 'a', encoding='utf-8') as f:
        f.write("\n添加更多内容")
    print(f"修改文件: {test_file}")
    time.sleep(0.5)
    
    # 3. 创建子目录
    sub_dir = os.path.join(folder_path, "subfolder")
    os.makedirs(sub_dir, exist_ok=True)
    print(f"创建目录: {sub_dir}")
    time.sleep(0.5)
    
    # 4. 在子目录中创建文件
    sub_file = os.path.join(sub_dir, "test2.txt")
    with open(sub_file, 'w', encoding='utf-8') as f:
        f.write("子目录中的测试文件")
    print(f"在子目录中创建文件: {sub_file}")
    time.sleep(0.5)
    
    # 5. 重命名文件
    new_file = os.path.join(folder_path, "renamed.txt")
    os.rename(test_file, new_file)
    print(f"重命名文件: {test_file} -> {new_file}")
    time.sleep(0.5)
    
    # 6. 删除文件
    os.remove(new_file)
    print(f"删除文件: {new_file}")
    time.sleep(0.5)
    
    # 7. 删除目录
    shutil.rmtree(sub_dir)
    print(f"删除目录: {sub_dir}")
    time.sleep(0.5)


def main():
    """主测试函数"""
    # 确保test_folder存在
    folder_path = "test_folder"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    # 清空文件夹（可选）
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isfile(item_path):
            os.remove(item_path)
        else:
            shutil.rmtree(item_path)
    
    print("文件夹监控程序测试")
    print("=" * 50)
    
    # 启动监控进程
    monitor_process = run_monitor("folder_monitor.py", folder_path)
    
    try:
        # 执行文件操作
        test_file_operations(folder_path)
        
        # 等待一段时间让监控程序捕获所有事件
        print("\n等待监控程序输出...")
        time.sleep(3)
        
        # 读取监控程序的输出
        print("\n监控程序输出:")
        print("-" * 30)
        while True:
            line = monitor_process.stdout.readline()
            if not line:
                break
            print(line.rstrip())
        
    finally:
        # 终止监控进程
        print("\n终止监控进程...")
        monitor_process.terminate()
        monitor_process.wait(timeout=2)
        if monitor_process.poll() is None:
            monitor_process.kill()
    
    print("\n测试完成！")


if __name__ == "__main__":
    main()