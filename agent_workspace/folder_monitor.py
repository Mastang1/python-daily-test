#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文件夹监控小程序
使用watchdog库监控指定文件夹中的文件变化，并在控制台打印相关信息
"""

import time
import sys
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class FolderMonitorHandler(FileSystemEventHandler):
    """自定义文件系统事件处理器"""

    def on_created(self, event):
        """当文件或目录被创建时调用"""
        if event.is_directory:
            print(f"[目录创建] {event.src_path}")
        else:
            print(f"[文件创建] {event.src_path}")
            self._print_file_info(event.src_path)

    def on_modified(self, event):
        """当文件或目录被修改时调用"""
        if event.is_directory:
            # 目录修改事件通常可以忽略
            pass
        else:
            print(f"[文件修改] {event.src_path}")
            self._print_file_info(event.src_path)

    def on_deleted(self, event):
        """当文件或目录被删除时调用"""
        if event.is_directory:
            print(f"[目录删除] {event.src_path}")
        else:
            print(f"[文件删除] {event.src_path}")

    def on_moved(self, event):
        """当文件或目录被移动/重命名时调用"""
        if event.is_directory:
            print(f"[目录移动] {event.src_path} -> {event.dest_path}")
        else:
            print(f"[文件移动] {event.src_path} -> {event.dest_path}")

    def _print_file_info(self, file_path):
        """打印文件的详细信息"""
        try:
            stat = os.stat(file_path)
            size = stat.st_size
            mtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(stat.st_mtime))
            print(f"    大小: {size} 字节")
            print(f"    修改时间: {mtime}")
        except Exception as e:
            print(f"    无法获取文件信息: {e}")


def monitor_folder(folder_path):
    """
    监控指定文件夹
    
    Args:
        folder_path: 要监控的文件夹路径
    """
    if not os.path.exists(folder_path):
        print(f"错误: 文件夹 '{folder_path}' 不存在")
        return
    
    if not os.path.isdir(folder_path):
        print(f"错误: '{folder_path}' 不是文件夹")
        return
    
    print(f"开始监控文件夹: {os.path.abspath(folder_path)}")
    print("按 Ctrl+C 停止监控")
    print("-" * 50)
    
    # 创建事件处理器和观察者
    event_handler = FolderMonitorHandler()
    observer = Observer()
    observer.schedule(event_handler, folder_path, recursive=True)
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n正在停止监控...")
        observer.stop()
    
    observer.join()
    print("监控已停止")


if __name__ == "__main__":
    # 默认监控当前目录下的 test_folder 文件夹
    target_folder = "test_folder"
    
    # 如果提供了命令行参数，使用第一个参数作为文件夹路径
    if len(sys.argv) > 1:
        target_folder = sys.argv[1]
    
    monitor_folder(target_folder)