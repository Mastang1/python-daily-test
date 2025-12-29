import time
import threading
import queue
from scapy.all import sniff, AsyncSniffer, conf
from scapy.layers.inet import IP, TCP, UDP
from scapy.layers.l2 import Ether

# 强制 Scapy 使用 Npcap 接口（Windows 必须）
conf.use_pcap = True

class ScapySniffer:
    def __init__(self, interface=None, bpf_filter="ip", output_queue_size=10000):
        """
        :param interface: 网卡名称，Windows下如果不指定，Scapy会自动寻找默认网卡
        :param bpf_filter: 过滤规则，例如 "tcp port 80"
        """
        self.interface = interface
        self.bpf_filter = bpf_filter
        self.packet_queue = queue.Queue(maxsize=output_queue_size)
        self.is_running = False
        self.sniffer = None
        self.process_thread = None
        
        self.stats = {'captured': 0, 'processed': 0, 'dropped': 0}

    def _packet_callback(self, packet):
        """生产者：这是 Scapy 抓到包后的回调，要极速处理，只塞队列"""
        try:
            self.packet_queue.put(packet, block=False)
            self.stats['captured'] += 1
        except queue.Full:
            self.stats['dropped'] += 1

    def _process_loop(self):
        """消费者：后台解析线程"""
        print("[*] 处理线程启动...")
        while self.is_running or not self.packet_queue.empty():
            try:
                # 获取数据包对象
                pkt = self.packet_queue.get(timeout=1)
                self._parse_packet(pkt)
                self.stats['processed'] += 1
                self.packet_queue.task_done()
            except queue.Empty:
                continue
            except Exception as e:
                print(f"[-] 处理异常: {e}")

    def _parse_packet(self, pkt):
        """解析逻辑"""
        try:
            # Scapy 的 pkt 对象已经解析好了，直接通过属性访问
            # 这里演示提取 IP 和 TCP/UDP 信息
            
            if not pkt.haslayer(IP):
                return

            ip_layer = pkt[IP]
            src_ip = ip_layer.src
            dst_ip = ip_layer.dst
            timestamp = pkt.time
            
            info = ""
            proto = ""

            if pkt.haslayer(TCP):
                proto = "TCP"
                tcp = pkt[TCP]
                flags = tcp.flags # S, A, F, R 等
                info = f"{tcp.sport} -> {tcp.dport} [{flags}]"
            elif pkt.haslayer(UDP):
                proto = "UDP"
                udp = pkt[UDP]
                info = f"{udp.sport} -> {udp.dport} Len={udp.len}"
            else:
                proto = "IP"

            print(f"[{float(timestamp):.4f}] {proto:<4} {src_ip:<15} -> {dst_ip:<15} : {info}")

        except Exception as e:
            print(f"Err: {e}")

    def start(self):
        self.is_running = True
        
        # 启动消费者线程
        self.process_thread = threading.Thread(target=self._process_loop, daemon=True)
        self.process_thread.start()

        print(f"[*] 开始抓包 (Filter: {self.bpf_filter})...")
        
        # 使用 AsyncSniffer 实现异步抓包（高性能模式）
        # store=False 表示不在内存保存所有包，防止内存溢出
        self.sniffer = AsyncSniffer(
            iface=self.interface,
            prn=self._packet_callback, # 回调函数
            filter=self.bpf_filter,
            store=False 
        )
        self.sniffer.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop()

    def stop(self):
        print("\n[*] 正在停止...")
        self.is_running = False
        if self.sniffer:
            self.sniffer.stop()
        if self.process_thread:
            self.process_thread.join()
        print(f"[*] 结束。统计: {self.stats}")

if __name__ == "__main__":
    # --- Windows 网卡选择提示 ---
    # Scapy 在 Windows 上有时网卡名很长，如果不指定 iface，它会自动选一个。
    # 如果想查看网卡列表，可以在交互式命令行输入: show_interfaces()
    
    sniffer = ScapySniffer(bpf_filter="tcp or udp")
    sniffer.start()