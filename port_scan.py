# 文件名请务必改成： vnc_port_scanner.py  或  scan_192_168_110_60.py
# 千万不要叫 logging.py / socket.py / threading.py

import socket
import threading
from concurrent.futures import ThreadPoolExecutor
import time
import sys

# 目标 IP
TARGET = "192.168.110.60"

# 常见 VNC 端口（含各种变种、加密、隧道、隐藏端口）
VNC_PORTS = [
    # 标准 VNC
    5900, 5901, 5902, 5903, 5904, 5905, 5906, 5907, 5908, 5909,
    # 超高位（常见隐藏）
    5910, 5920, 5930, 5940, 5950, 5960, 5970, 5980, 5990,
    # 加密 VNC（如 VeNCrypt、TLS-VNC）
    5900,  # 通常还是走5900，但加密
    # 反向 VNC / 隧道 / 代理常见端口
    5500,       # RealVNC 旧版
    5800,       # VNC over HTTP (Java Viewer)
    5900 + 100, # 6000 — 常见偏移
    6080,       # noVNC (WebSocket)
    6081, 6082, # noVNC 变种
    # 极客最爱藏的端口
    3399,       # 伪装成 RDP+1
    8081,       # 伪装 Web
    8888,       # 常见开发端口
    9000, 9001,
    9999, 10000,
    12345,      # NetBus 经典后门（常被 VNC 复用）
    13720, 13721, 13722,  # TightVNC / UltraVNC 常见
    54321,      # 倒序经典
]

# 去重 + 排序
VNC_PORTS = sorted(set(VNC_PORTS))

# 常见端口（选项1）
COMMON_PORTS = [21,22,23,25,53,80,110,135,139,443,445,1433,3306,3389,5432,6379,8080,8443]

def scan_port(ip, port, timeout=0.8):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((ip, port))
        sock.close()
        if result == 0:
            return port, True
    except:
        pass
    return port, False

def scan_ports(ports, label="端口", threads=200, timeout=0.8):
    print(f"[+] 正在扫描 {TARGET} 的 {label}（共 {len(ports)} 个端口）...")
    start = time.time()
    open_ports = []
    
    with ThreadPoolExecutor(max_workers=threads) as executor:
        results = executor.map(lambda p: scan_port(TARGET, p, timeout), ports)
    
    for port, is_open in results:
        if is_open:
            banner = "可能为 VNC" if port in VNC_PORTS else ""
            print(f"    [OPEN] {port:5d}/tcp  开放  {banner}")
            open_ports.append(port)
    
    elapsed = time.time() - start
    print(f"[+] 扫描完成，用时 {elapsed:.2f} 秒，开放端口：{len(open_ports)} 个\n")
    return open_ports

# ==================== 主菜单 ====================
if __name__ == "__main__":
    print("=" * 62)
    print("    192.168.110.60 专用端口扫描器（VNC 专项加强版）")
    print("=" * 62)
    
    while True:
        print("\n请选择扫描模式：")
        print("  1. 扫描常见服务端口（HTTP/SSH/RDP/MySQL等）")
        print("  2. 扫描全端口 1-65535（极慢，仅用于最终确认）")
        print("  3. 快速扫描可能存在的 VNC 端口（强力推荐！）")
        print("  4. 退出")
        
        choice = input("\n请输入选项 (1-4): ").strip()
        
        if choice == "1":
            scan_ports(COMMON_PORTS, "常见服务端口", threads=150)
            
        elif choice == "3":
            print("\n【VNC 专项扫描启动】正在探测标准、隐藏、加密、隧道等所有可能存在的 VNC...")
            open_vnc = scan_ports(VNC_PORTS, "VNC 相关端口", threads=300, timeout=0.7)
            if open_vnc:
                print(f"  发现 {len(open_vnc)} 个疑似 VNC 端口！建议立即用 VNC Viewer 连接测试：")
                for p in sorted(open_vnc):
                    if p >= 5900 and p <= 5999:
                        display = p - 5900
                        print(f"     → {TARGET}:{p}  (Display :{display})  ← 极大概率是真实 VNC！")
                    else:
                        print(f"     → {TARGET}:{p}")
            else:
                print("  未发现常见 VNC 端口，可能是未开启或使用了非常隐蔽端口")
                
        elif choice == "2":
            confirm = input("\n[!] 全端口扫描非常慢，可能需要 5-15 分钟，确定要继续？(y/N): ")
            if confirm.lower() == 'y':
                all_ports = list(range(1, 65536))
                scan_ports(all_ports, "全端口 1-65535", threads=1000, timeout=0.3)
            else:
                print("已取消")
                
        elif choice == "4" or choice.lower() == "q":
            print("再见！扫描结束")
            break
            
        else:
            print("无效选项，请输入 1-4")