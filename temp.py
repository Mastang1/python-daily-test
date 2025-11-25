#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
C/C++ 工程代码一键打包工具（专为喂给 Grok 等大模型设计）

用法示例：
    python pack_code.py ./my_project
    python pack_code.py ../src -o packed_code.txt -e .c .h .cpp .hpp .cc
    python pack_code.py ./firmware --ignore "build" "obj" ".git"
"""

import argparse
import os
import sys
from pathlib import Path
from typing import List


def collect_files(root_dir: Path, extensions: List[str], ignore_dirs: List[str]) -> List[Path]:
    """递归收集指定扩展名的文件，排除忽略目录"""
    root_dir = root_dir.resolve()
    files = []
    
    for file_path in root_dir.rglob('*'):
        if not file_path.is_file():
            continue
            
        # 跳过忽略的目录
        if any(ignored in file_path.resolve().parts for ignored in ignore_dirs):
            continue
            
        if extensions and file_path.suffix.lower() not in [ext.lower() for ext in extensions]:
            continue
            
        files.append(file_path)
    
    # 按相对路径排序，保证每次打包顺序一致（方便对比）
    files.sort(key=lambda p: str(p.relative_to(root_dir)))
    return files


def pack_code(source_dir: str, 
              output_file: str = "all_code.txt",
              extensions: List[str] = None,
              ignore_dirs: List[str] = None,
              encoding: str = "utf-8") -> None:
    """
    把整个工程的源码打包成一个文件，每文件前带分隔线
    """
    if extensions is None:
        extensions = [".c", ".h", ".cpp", ".hpp", ".cc", ".cxx", ".hh"]
    
    if ignore_dirs is None:
        ignore_dirs = ["build", "obj", "Debug", "Release", ".git", "__pycache__", "node_modules"]
    else:
        ignore_dirs = ignore_dirs + ["build", "obj", "Debug", "Release", ".git", "__pycache__", "node_modules"]
    
    root = Path(source_dir)
    if not root.exists():
        print(f"错误：目录不存在 → {source_dir}")
        sys.exit(1)
    
    files = collect_files(root, extensions, ignore_dirs)
    
    if not files:
        print("警告：没有找到任何匹配的文件！")
        return
    
    total_files = len(files)
    print(f"正在打包 {total_files} 个文件 → {output_file}")
    
    with open(output_file, "w", encoding=encoding, errors="replace") as out:
        out.write(f"# 项目路径: {root.resolve()}\n")
        out.write(f"# 打包时间: {os.popen('date').read().strip()}\n")
        out.write(f"# 共打包 {total_files} 个源文件\n")
        out.write("#" + "="*80 + "\n\n")
        
        for i, file_path in enumerate(files, 1):
            rel_path = file_path.relative_to(root)
            separator = f"===== 文件 [{i}/{total_files}]: {rel_path} ====="
            out.write(separator + "\n")
            try:
                content = file_path.read_text(encoding=encoding, errors="replace")
                out.write(content)
                if not content.endswith("\n"):
                    out.write("\n")
            except Exception as e:
                out.write(f"\n!!! 读取失败: {e}\n")
            out.write("\n\n")
    
    print(f"打包完成！共 {total_files} 个文件，已保存到：{output_file}")
    print(f"直接复制该文件内容喂给 Grok 即可～")


def main():
    parser = argparse.ArgumentParser(description="C/C++ 工程代码打包工具（专为 Grok 分析设计）")
    parser.add_argument("path", help="要打包的工程目录路径")
    parser.add_argument("-o", "--output", default="all_code.txt", help="输出文件名（默认: all_code.txt）")
    parser.add_argument("-e", "--ext", nargs="+", 
                        help="要打包的文件扩展名，例如 .c .h .cpp（默认包含常见 C/C++ 扩展名）")
    parser.add_argument("--ignore", nargs="+", 
                        help="额外要忽略的目录名（如 build .git）")
    parser.add_argument("--encoding", default="utf-8", help="文件编码（默认 utf-8）")
    
    args = parser.parse_args()
    
    pack_code(
        source_dir=args.path,
        output_file=args.output,
        extensions=args.ext,
        ignore_dirs=args.ignore,
        encoding=args.encoding
    )


if __name__ == "__main__":
    main()