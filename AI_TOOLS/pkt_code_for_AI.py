#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
C/C++ 工程代码一键打包工具（增强版）
新增功能：智能排除二进制文件（.o, .bin, .hex, .elf, 以及任何隐藏的二进制文件）
"""

import argparse
import os
import sys
import chardet
from pathlib import Path
from typing import List


def is_binary_file(file_path: Path, block_size: int = 1024) -> bool:
    """
    智能检测文件是否为二进制文件
    方法：读取前 block_size 字节
    - 如果包含 \0（null byte），极大概率是二进制
    - 再结合 chardet 检测，如果置信度低或检测为 binary，直接判定为二进制
    """
    try:
        with file_path.open("rb") as f:
            chunk = f.read(block_size)
            if not chunk:
                return False  # 空文件算文本

            # 方法1：包含空字节 → 几乎100%是二进制
            if b'\0' in chunk:
                return True

            # 方法2：尝试解码 + chardet 检测
            try:
                text = chunk.decode('utf-8', errors='strict')
                # utf-8 能正常解码的不太可能是二进制
                return False
            except UnicodeDecodeError:
                # 解码失败，再用 chardet 判断
                result = chardet.detect(chunk)
                if result['encoding'] is None or result['confidence'] < 0.7:
                    return True
                # 某些二进制文件可能被误判为 ascii，保险起见再检查是否有高位控制字符
                control_chars = sum(1 for c in chunk if 0 < c < 32 and c != 9 and c != 10 and c != 13)
                if control_chars > len(chunk) * 0.3:  # 控制字符超过30%
                    return True
                return False
    except Exception:
        return True  # 读取失败，保守起见当作二进制跳过


def is_likely_source_file(file_path: Path) -> bool:
    """额外判断常见二进制扩展名，直接排除"""
    binary_extensions = {
        '.o', '.obj', '.a', '.lib', '.so', '.dll', '.exe',
        '.bin', '.hex', '.elf', '.axf', '.out',
        '.png', '.jpg', '.jpeg', '.gif', '.bmp', '.ico',
        '.pdf', '.zip', '.7z', '.rar', '.tar', '.gz',
        '.wav', '.mp3', '.mp4', '.avi',
    }
    return file_path.suffix.lower() not in binary_extensions


def collect_files(root_dir: Path, extensions: List[str], ignore_dirs: List[str]) -> List[Path]:
    """递归收集源码文件，严格排除二进制"""
    root_dir = root_dir.resolve()
    files = []

    for file_path in root_dir.rglob('*'):
        if not file_path.is_file():
            continue

        # 跳过忽略目录
        if any(ignored in file_path.resolve().parts for ignored in ignore_dirs):
            continue

        # 扩展名白名单（如果指定了）
        if extensions:
            if file_path.suffix.lower() not in [ext.lower() for ext in extensions]:
                continue
        else:
            # 没指定扩展名时，也要排除明显不是源码的
            if not is_likely_source_file(file_path):
                continue

        # 最终防线：二进制检测
        if is_binary_file(file_path):
            print(f"跳过二进制文件: {file_path.relative_to(root_dir)}")
            continue

        files.append(file_path)

    files.sort(key=lambda p: str(p.relative_to(root_dir)))
    return files


# ====================== 下面是主函数（和之前基本一样） ======================

def pack_code(source_dir: str,
              output_file: str = "all_code.txt",
              extensions: List[str] = None,
              ignore_dirs: List[str] = None,
              encoding: str = "utf-8") -> None:

    if extensions is None:
        extensions = [".c", ".h", ".cpp", ".hpp", ".cc", ".cxx", ".hh", ".inc", ".s", ".S"]

    default_ignore = ["build", "obj", "Debug", "Release", ".git", "__pycache__", "node_modules", ".vscode", ".idea"]
    ignore_dirs = (ignore_dirs or []) + default_ignore

    root = Path(source_dir)
    if not root.exists():
        print(f"错误：目录不存在 → {source_dir}")
        sys.exit(1)

    print("正在扫描并过滤二进制文件，请稍等...")
    files = collect_files(root, extensions, ignore_dirs)

    if not files:
        print("警告：没有找到任何合法的源代码文件！")
        return

    print(f"正在打包 {len(files)} 个源码文件 → {output_file}")

    with open(output_file, "w", encoding=encoding, errors="replace") as out:
        out.write(f"# 项目路径: {root.resolve()}\n")
        out.write(f"# 打包时间: {os.popen('date').read().strip()}\n")
        out.write(f"# 共打包 {len(files)} 个源文件（已自动排除二进制文件）\n")
        out.write("#" + "="*80 + "\n\n")

        for i, file_path in enumerate(files, 1):
            rel_path = file_path.relative_to(root)
            separator = f"===== 文件 [{i}/{len(files)}]: {rel_path} ====="
            out.write(separator + "\n")
            try:
                content = file_path.read_text(encoding=encoding, errors="replace")
                out.write(content.rstrip() + "\n")  # 确保结尾有换行
            except Exception as e:
                out.write(f"\n!!! 读取失败: {e}\n")
            out.write("\n\n")

    print(f"打包完成！100% 纯文本，已安全排除所有二进制文件")
    print(f"输出文件：{output_file}")
    print(f"现在可以放心复制整个文件内容喂给 Grok 了！")


def main():
    parser = argparse.ArgumentParser(description="C/C++ 工程代码打包工具（防二进制污染增强版）")
    parser.add_argument("path", help="要打包的工程目录路径")
    parser.add_argument("-o", "--output", default="all_code.txt", help="输出文件名（默认: all_code.txt）")
    parser.add_argument("-e", "--ext", nargs="+", help="只打包指定扩展名（如 .c .h）")
    parser.add_argument("--ignore", nargs="+", help="额外忽略的目录")
    parser.add_argument("--encoding", default="utf-8", help="文件编码")

    args = parser.parse_args()

    # 自动安装 chardet（如果没装的话）
    try:
        import chardet
    except ImportError:
        print("正在安装依赖：chardet（用于二进制检测）...")
        os.system(f"{sys.executable} -m pip install --quiet chardet")
        import chardet

    pack_code(
        source_dir=args.path,
        output_file=args.output,
        extensions=args.ext,
        ignore_dirs=args.ignore,
        encoding=args.encoding
    )


if __name__ == "__main__":
    main()