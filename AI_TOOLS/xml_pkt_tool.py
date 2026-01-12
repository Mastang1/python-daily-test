#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
代码工程一键打包工具（Gemini/LLM 优化版）
功能：
1. 支持 .c, .h, .xml, .xdm 等多种后缀。
2. 智能排除二进制文件。
3. 生成包含特定提示词（Prompt）的整合包，方便 AI 识别和拆分。
"""

import argparse
import os
import sys
import datetime
from pathlib import Path
from typing import List

# 尝试导入 chardet，如果不存在则后续处理
try:
    import chardet
    HAS_CHARDET = True
except ImportError:
    HAS_CHARDET = False

def is_binary_file(file_path: Path, block_size: int = 1024) -> bool:
    """
    智能检测文件是否为二进制文件
    """
    try:
        with file_path.open("rb") as f:
            chunk = f.read(block_size)
            if not chunk:
                return False

            # 1. 空字节检测 (最强特征)
            if b'\0' in chunk:
                return True

            # 2. 尝试 UTF-8 解码
            try:
                chunk.decode('utf-8', errors='strict')
                return False
            except UnicodeDecodeError:
                pass

            # 3. 如果有 chardet，利用它检测
            if HAS_CHARDET:
                result = chardet.detect(chunk)
                if result['confidence'] < 0.7:
                    return True
            
            # 4. 统计控制字符 (兜底方案)
            # 排除常见空白符: 9(TAB), 10(LF), 13(CR)
            text_chars = bytearray({7, 8, 9, 10, 12, 13, 27} | set(range(0x20, 0x100)) - {0x7f})
            if not all(c in text_chars for c in chunk):
                # 如果包含非文本字符的比例过高
                non_text = sum(1 for c in chunk if c not in text_chars)
                if non_text / len(chunk) > 0.3:
                    return True

            return False
    except Exception:
        return True

def collect_files(root_dir: Path, extensions: List[str], ignore_dirs: List[str]) -> List[Path]:
    """收集文件并过滤"""
    root_dir = root_dir.resolve()
    files = []

    # 常见二进制后缀黑名单 (即使在白名单扩展名里，如果是这些后缀也强制排除)
    binary_ext_blacklist = {
        '.o', '.obj', '.a', '.lib', '.so', '.dll', '.exe',
        '.bin', '.hex', '.elf', '.axf', '.out', '.pyc',
        '.png', '.jpg', '.jpeg', '.gif', '.ico', '.pdf', '.zip'
    }

    for file_path in root_dir.rglob('*'):
        if not file_path.is_file():
            continue

        # 排除忽略目录
        if any(ignored in file_path.parts for ignored in ignore_dirs):
            continue

        suffix = file_path.suffix.lower()

        # 扩展名过滤
        if extensions:
            # 如果指定了扩展名列表，必须匹配
            if suffix not in [e.lower() for e in extensions]:
                continue
        else:
            # 如果没指定，排除显式的二进制后缀
            if suffix in binary_ext_blacklist:
                continue

        # 内容检测
        if is_binary_file(file_path):
            # print(f"DEBUG: 跳过二进制内容: {file_path.name}")
            continue

        files.append(file_path)

    # 按路径排序，保证输出顺序稳定
    files.sort(key=lambda p: str(p.relative_to(root_dir)))
    return files

def generate_ai_prompt(file_count: int, root_path: Path) -> str:
    """
    生成专门给 Gemini/LLM 看的头部提示词
    """
    date_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"""
==============================================================================
[CONTEXT FOR AI ASSISTANT]
You are processing a packed codebase containing {file_count} source files.
Project Root: {root_path.name}
Packed Date: {date_str}

[INSTRUCTIONS]
1. The code below contains multiple files packed into a single text block.
2. Each file is demarcated by a START header and an END footer.
3. The format is:
   ========== START FILE: <relative_path> ==========
   <file_content>
   ========== END FILE: <relative_path> ==========
4. When analyzing, strictly distinguish between separate files based on these markers.
5. If asked to modify, please reference the specific file path provided in the header.

[FILE LIST]
"""

def pack_code(source_dir: str,
              output_file: str = "project_packed.txt",
              extensions: List[str] = None,
              ignore_dirs: List[str] = None,
              encoding: str = "utf-8") -> None:

    # 默认支持的扩展名（包含 C/C++, XML, XDM）
    if extensions is None:
        extensions = [
            ".c", ".h", ".cpp", ".hpp", ".cc", ".cxx", 
            ".xml", ".xdm", 
            ".py", ".sh", ".json", ".yaml", ".md"
        ]

    default_ignore = [
        "build", "obj", "bin", "Debug", "Release", 
        ".git", ".svn", "__pycache__", ".vscode", ".idea", "node_modules"
    ]
    ignore_dirs = (ignore_dirs or []) + default_ignore

    root = Path(source_dir)
    if not root.exists():
        print(f"错误：路径不存在 {source_dir}")
        return

    print(f"正在扫描: {root}")
    files = collect_files(root, extensions, ignore_dirs)

    if not files:
        print("未找到符合条件的源码文件。")
        return

    print(f"找到 {len(files)} 个文件，准备打包...")

    try:
        with open(output_file, "w", encoding=encoding, errors="replace") as out:
            # 1. 写入 AI 引导提示词
            prompt = generate_ai_prompt(len(files), root)
            out.write(prompt)
            
            # 写入文件清单
            for f in files:
                out.write(f"- {f.relative_to(root)}\n")
            out.write("==============================================================================\n\n")

            # 2. 写入文件内容
            for i, file_path in enumerate(files, 1):
                rel_path = file_path.relative_to(root)
                # 使用非常明确的起始和结束标记，方便 AI 解析
                header = f"========== START FILE: {rel_path} =========="
                footer = f"========== END FILE: {rel_path} =========="
                
                out.write(f"{header}\n")
                try:
                    content = file_path.read_text(encoding=encoding, errors="replace")
                    # 确保内容不是空的，并且末尾有换行
                    if content:
                        out.write(content)
                        if not content.endswith("\n"):
                            out.write("\n")
                except Exception as e:
                    out.write(f"[ERROR READING FILE: {e}]\n")
                
                out.write(f"{footer}\n\n")

        print(f"打包成功！")
        print(f"输出文件: {output_file}")
        print(f"包含文件类型: {extensions}")
        print("提示：已加入 AI 专用提示词，可直接发送给 Gemini。")

    except IOError as e:
        print(f"写入文件失败: {e}")

def main():
    parser = argparse.ArgumentParser(description="代码打包工具（支持 C/H/XML/XDM 等，AI 友好型）")
    parser.add_argument("path", help="工程根目录")
    parser.add_argument("-o", "--output", default="code_context.txt", help="输出文件名")
    parser.add_argument("-e", "--ext", nargs="+", help="指定后缀 (例如: .c .h .xml .xdm)")
    parser.add_argument("--ignore", nargs="+", help="额外忽略的文件夹")

    args = parser.parse_args()

    # 如果用户没装 chardet，提示一下但不强制退出（代码里有兜底逻辑）
    if not HAS_CHARDET:
        print("提示: 未检测到 chardet 库，将使用基础算法检测二进制文件。")
        print("建议安装: pip install chardet\n")

    pack_code(
        source_dir=args.path,
        output_file=args.output,
        extensions=args.ext,
        ignore_dirs=args.ignore
    )

if __name__ == "__main__":
    main()