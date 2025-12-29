`AsyncSniffer` 中的 `filter` 参数使用的是 **BPF (Berkeley Packet Filter)** 语法。

这是网络工程中最通用的标准（Tcpdump、Wireshark 的抓包过滤器、libpcap 底层都用它）。它的核心优势是：**在内核层直接过滤**，不符合规则的数据包根本不会拷贝到 Python 内存中，**性能极高**。

以下是工程中常用的 BPF 过滤参数列表，按使用场景分类：

### 1. 基于 IP / 主机 (Host)

最常用的过滤方式，用于锁定通信目标。

| 语法示例 | 说明 |
| --- | --- |
| `host 192.168.1.100` | 抓取源 **或** 目的 IP 是 192.168.1.100 的所有包 |
| `src host 192.168.1.100` | 仅抓取 **来自** 该 IP 的包 (Source) |
| `dst host 192.168.1.100` | 仅抓取 **发往** 该 IP 的包 (Destination) |
| `net 192.168.1.0/24` | 抓取整个网段的包 (CIDR格式) |
| `ether host 00:11:22:33:44:55` | 根据 MAC 地址过滤 (适合二层分析) |

### 2. 基于端口 (Port)

用于区分服务（HTTP, DNS, Modbus 等）。

| 语法示例 | 说明 |
| --- | --- |
| `port 80` | 抓取源 **或** 目的端口是 80 的包 |
| `src port 80` | 仅抓取源端口是 80 的包 |
| `dst port 80` | 仅抓取目的端口是 80 的包 |
| `portrange 8000-8085` | 抓取端口在 8000 到 8085 之间的包 |

### 3. 基于协议 (Protocol)

用于过滤特定类型的流量。

| 语法示例 | 说明 |
| --- | --- |
| `ip` | 仅 IPv4 |
| `ip6` | 仅 IPv6 |
| `tcp` | 仅 TCP 流量 |
| `udp` | 仅 UDP 流量 |
| `icmp` | 仅 Ping 包等 ICMP 流量 |
| `arp` | 仅 ARP 广播/应答 |
| `ether proto 0x88B8` | 抓取特定以太网协议类型 (例如 GOOSE, EtherCAT 等工业协议) |

### 4. 逻辑组合 (Logical Operators)

**这是工程级代码最核心的部分**，通过组合实现精准过滤，避免抓到垃圾数据。

| 关键词 | 符号 | 说明 |
| --- | --- | --- |
| `and` | `&&` | 与：必须同时满足 |
| `or` | `||` | 或：满足其中之一即可 |
| `not` | `!` | 非：排除特定条件 |

**组合示例：**

* **只看 Web 流量：**
`tcp port 80 or tcp port 443`
* **排除 SSH 干扰（非常常用）：**
`not port 22`
* **精准定位某台机器的特定服务：**
`host 192.168.1.50 and tcp port 502` (例如抓取某台 PLC 的 Modbus 流量)
* **排除广播包：**
`not broadcast and not multicast`

### 5. 高级/特殊过滤 (Advanced)

当基本参数不够用时，可以直接检查包的长度或特定字节。

| 语法示例 | 说明 |
| --- | --- |
| `len > 100` | 抓取长度大于 100 字节的包 |
| `less 64` | 抓取长度小于 64 字节的包 |
| `broadcast` | 仅抓取广播包 (目标 MAC 为 FF:FF:FF:FF:FF:FF) |
| `multicast` | 仅抓取组播包 |
| `tcp[tcpflags] & tcp-syn != 0` | **高阶用法**：仅抓取 TCP SYN 握手包（常用于扫描检测） |

---

### 重要提示：不要混淆 BPF 和 Wireshark 过滤器

* **Capture Filter (BPF):** Scapy 和 `filter` 参数用的就是这个。语法是 `host x.x.x.x`。
* **Display Filter (Wireshark 上方输入框):** 语法是 `ip.addr == x.x.x.x`。
* **切记：** 在 Scapy 代码中**只能使用 BPF 语法**，不能用 `==` 这种写法。

### 工程实战推荐配置

如果你在做通用的以太网消息抓取工具，我建议默认使用以下策略：

1. **默认过滤 SSH/RDP：** 开发调试时，自己的远程连接流量会刷屏，建议加上 `not port 22 and not port 3389`。
2. **过滤掉本地回环：** 如果只关心外部流量，加上 `not host 127.0.0.1`。

**代码示例：**

```python
# 抓取本机和 192.168.1.100 之间的 HTTP 通信，且排除空包
bpf_filter = "host 192.168.1.100 and tcp port 80 and len > 0"

self.sniffer = AsyncSniffer(
    # ...
    filter=bpf_filter,
    # ...
)

```