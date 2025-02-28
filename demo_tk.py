import tkinter as tk
from tkinter import messagebox
import json

# 统一的通信设备API类
class CommunicationDevice:
    def __init__(self):
        self.parameters = {}

    def open(self):
        pass

    def close(self):
        pass

    def write(self, data):
        pass

    def read(self):
        pass

# CAN设备类
class CANDevice(CommunicationDevice):
    def __init__(self):
        super().__init__()
        self.parameters = {
            "channel": 0,
            "bitrate": 500000
        }

    def specific_function(self):
        pass

# UART设备类
class UARTDevice(CommunicationDevice):
    def __init__(self):
        super().__init__()
        self.parameters = {
            "baudrate": 9600,
            "parity": "N",
            "stopbits": 1
        }

    def specific_function(self):
        pass

# 生成交互对话框
def generate_dialog(device):
    root = tk.Tk()
    root.title("Device Parameters")

    entries = {}
    row = 0
    for key, value in device.parameters.items():
        tk.Label(root, text=key).grid(row=row, column=0)
        entry = tk.Entry(root)
        entry.insert(0, str(value))
        entry.grid(row=row, column=1)
        entries[key] = entry
        row += 1

    def save_parameters():
        for key, entry in entries.items():
            try:
                value = int(entry.get()) if isinstance(device.parameters[key], int) else entry.get()
                device.parameters[key] = value
            except ValueError:
                messagebox.showerror("Error", f"Invalid value for {key}")
                return
        root.destroy()

    tk.Button(root, text="Save", command=save_parameters).grid(row=row, column=0, columnspan=2)

    root.mainloop()

# 生成设备API调用程序
def generate_api_call(device):
    api_call = f"device = {device.__class__.__name__}()\n"
    for key, value in device.parameters.items():
        api_call += f"device.parameters['{key}'] = {repr(value)}\n"
    api_call += "device.open()\n"
    api_call += "data = 'test data'\n"
    api_call += "device.write(data)\n"
    api_call += "response = device.read()\n"
    api_call += "device.close()\n"
    return api_call

# 从Python程序中读取参数并重新呈现对话框
def read_parameters_from_code(code):
    lines = code.split('\n')
    parameters = {}
    for line in lines:
        if "device.parameters" in line:
            key = line.split("'")[1]
            value = eval(line.split("=")[1].strip())
            parameters[key] = value
    return parameters

def main():
    # 选择设备
    device = CANDevice()  # 可以替换为UARTDevice()

    # 生成交互对话框
    generate_dialog(device)

    # 生成设备API调用程序
    api_call = generate_api_call(device)
    print(api_call)

    # 保存API调用程序到文件
    with open("device_api_call.py", "w") as f:
        f.write(api_call)

    # 从文件中读取API调用程序
    with open("device_api_call.py", "r") as f:
        code = f.read()

    # 读取参数并重新呈现对话框
    parameters = read_parameters_from_code(code)
    device.parameters = parameters
    generate_dialog(device)

if __name__ == "__main__":
    main()
