import ctypes
import sys
import time

def set_console_window(title="Nikola Tesla", width=800, height=600, x=100, y=100):
    """
    设置控制台窗口大小和位置
    """
    # 获取控制台窗口句柄
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    
    if hwnd:
        # 设置窗口标题
        ctypes.windll.kernel32.SetConsoleTitleW(title)
        
        # 设置窗口位置和大小
        ctypes.windll.user32.SetWindowPos(hwnd, 0, x, y, width, height, 0x0040)
        
        # 获取屏幕尺寸
        user32 = ctypes.windll.user32
        screen_width = user32.GetSystemMetrics(0)
        screen_height = user32.GetSystemMetrics(1)
        
        # 确保窗口在屏幕范围内
        if x + width > screen_width:
            x = screen_width - width
        if y + height > screen_height:
            y = screen_height - height
            
        # 重新设置位置
        ctypes.windll.user32.SetWindowPos(hwnd, 0, x, y, width, height, 0x0040)
        
        return True
    return False

def print_continuous_message():
    """
    以1ms间隔持续打印消息
    """
    try:
        while True:
            print("today is a nice day!")
            time.sleep(0.0004)  # 1ms间隔
    except KeyboardInterrupt:
        print("\n程序已停止")

# 使用示例
if __name__ == "__main__":
    set_console_window("我的应用控制台", 1000, 700, 200, 150)
    print_continuous_message()