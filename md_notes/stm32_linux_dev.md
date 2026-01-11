下面我把 **“Ubuntu + VSCode 搭建 STM32 开发环境（从零开始）”** 整理成一份 **完整、可直接保存为 `.md` 文件的 Markdown 文档**。
文档内容 **不包含我们的聊天语气**，完全是工程化说明书风格，便于长期保存与查阅。

你只需要把下面内容 **整段复制到你的编辑器（VSCode/Obsidian/Notion）** 保存为：

```
stm32_ubuntu_setup.md
```

即可。

---

# **Ubuntu + VSCode 搭建 STM32 开发环境（完整指南）**

本手册介绍如何在 **Ubuntu + VS Code** 环境下，从零开始搭建 STM32 开发环境，包括编译器、调试器、工程结构和 VS Code 调试配置。

适用于 STM32F1 / F4 / F7 / G4 / H7 等所有 ARM Cortex-M 系列 MCU。

---

# 1. 安装 ARM 交叉编译工具链（arm-none-eabi-gcc）

Ubuntu 可以直接安装官方 GCC：

```bash
sudo apt update
sudo apt install gcc-arm-none-eabi gdb-multiarch
```

验证编译器：

```bash
arm-none-eabi-gcc --version
```

若需新版（如 12.x / 13.x），可从 ARM 官网下载压缩包手动安装。

---

# 2. 安装调试工具

根据调试器选择：ST-Link 或 JLink。

## 2.1 安装 OpenOCD（ST-Link）

```bash
sudo apt install openocd
```

验证：

```bash
openocd -v
```

## 2.2 安装 JLink（如果使用 JLink 调试器）

从 Segger 官网下载 Linux 版本 deb 包：

[https://www.segger.com/downloads/jlink/](https://www.segger.com/downloads/jlink/)

安装：

```bash
sudo dpkg -i JLink_Linux*.deb
```

---

# 3. 安装 VS Code 扩展

打开 VS Code → 扩展（Ctrl+Shift+X），安装：

* C/C++（Microsoft）
* Cortex-Debug
* CMake Tools
* Markdown All in One（可选）

**Cortex-Debug** 用于在 VS Code 内通过 OpenOCD/JLink 调试 STM32。

---

# 4. 创建 STM32 最小工程（CMake 架构）

以下工程结构可直接用于 STM32F103C8，也可根据芯片修改：

```
stm32_project/
├── CMakeLists.txt
├── src/
│   └── main.c
├── linker/
│   └── STM32F103C8_FLASH.ld
├── startup/
│   └── startup_stm32f103xb.s
└── build/
```

---

# 5. CMakeLists.txt 示例（裸机工程）

以下为一个最小可编译的 STM32 CMake 配置：

```cmake
cmake_minimum_required(VERSION 3.13)

project(stm32-minimal C CXX ASM)

set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)

set(CPU_FLAGS "-mcpu=cortex-m3 -mthumb")
set(LINKER_SCRIPT ${CMAKE_SOURCE_DIR}/linker/STM32F103C8_FLASH.ld)

add_executable(${PROJECT_NAME}
    src/main.c
    startup/startup_stm32f103xb.s
)

target_compile_options(${PROJECT_NAME} PRIVATE
    ${CPU_FLAGS}
    -O2
    -ffreestanding
    -Wall -Wextra
)

target_link_options(${PROJECT_NAME} PRIVATE
    ${CPU_FLAGS}
    -T${LINKER_SCRIPT}
    -Wl,--gc-sections
)
```

---

# 6. 最小 main.c 示例

```c
#include "stm32f10x.h"

int main(void)
{
    RCC->APB2ENR |= RCC_APB2ENR_IOPCEN; 
    GPIOC->CRH &= ~(0xF << (13*4-32));  
    GPIOC->CRH |=  (0x1 << (13*4-32));  

    while (1) {
        GPIOC->ODR ^= (1 << 13);
        for (volatile int i = 0; i < 50000; i++);
    }
}
```

需要配套 CMSIS 文件。

---

# 7. 编译工程

在项目根目录执行：

```bash
mkdir build
cd build
cmake ..
make -j
```

生成：

* `.elf`
* `.bin`
* `.map`（视配置而定）

---

# 8. VS Code 调试配置文件

在根目录创建 `.vscode/launch.json`：

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Debug STM32",
            "type": "cortex-debug",
            "request": "launch",
            "servertype": "openocd",
            "cwd": "${workspaceFolder}",
            "executable": "build/stm32-minimal.elf",
            "device": "STM32F103C8",
            "configFiles": [
                "interface/stlink.cfg",
                "target/stm32f1x.cfg"
            ]
        }
    ]
}
```

调试方式：

* F5 启动调试
* 自动烧录，并在 main 处停下
* 支持寄存器、内存、断点、单步、FreeRTOS 线程显示

---

# 9. （可选）使用 STM32CubeMX 生成 HAL 工程 + CMake

STM32CubeMX 默认生成 Makefile 工程。
若需要 CMake，可引入第三方模板或自行添加 CMakeLists.txt。

---

# 10. （可选）使用 PlatformIO

更适合初学者和快速项目，功能包括：

* 自动下载工具链
* 自动生成工程
* 一键烧录和调试
* 提供 HAL 支持

VS Code 中安装 PlatformIO 插件即可使用。

---

# 11. 最终推荐的整体开发方案

建议使用：

**VSCode + CMake + arm-none-eabi-gcc + OpenOCD（或 JLink）**

这是目前国际上最主流、现代化、可维护性高的 STM32 开发工作流。

---

# 12. 扩展

若需要进一步内容，可以继续添加：

* FreeRTOS + STM32 的 CMake 工程模板
* OpenOCD cfg 文件
* JLink 调试配置
* STM32 HAL 工程模板
* STM32G4/F4/H7 等不同芯片的启动文件与链接脚本模板

---

以上即 Markdown 文件内容，可直接保存。

如你愿意，我也可以把 **调试图示、文件结构树、完整 CMake 工程模板** 加入文档，让这份 Markdown 更像专业文档。
