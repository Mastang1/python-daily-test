import argparse
import sys
from pathlib import Path

def setup_argparse():
    """
    配置命令行参数解析器
    """
    parser = argparse.ArgumentParser(
        description="Markdown 文件合并工具：将指定文件夹下的所有 .md 文件按名称升序合并为一个文件。",
        usage="python merge_md.py -ff <input_folder> -o <output_file>",
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument(
        '-ff', '--folder',
        type=str,
        required=True,
        help="指定包含 markdown 文件的原始文件夹路径 (例如: ./docs)"
    )

    parser.add_argument(
        '-o', '--output',
        type=str,
        required=True,
        help="指定输出文件的完整路径和文件名 (例如: ./output/merged.md)"
    )

    return parser

def merge_markdown_files(input_folder: Path, output_file: Path):
    """
    执行合并逻辑
    """
    # 1. 校验输入文件夹是否存在
    if not input_folder.exists() or not input_folder.is_dir():
        print(f"❌ 错误: 输入文件夹不存在或不是一个目录: {input_folder}")
        sys.exit(1)

    # 2. 获取所有 .md 文件并按文件名称升序排列
    # 使用 list comprehension 获取文件，然后 sorted 排序
    md_files = sorted([f for f in input_folder.glob("*.md") if f.is_file()], key=lambda x: x.name)

    if not md_files:
        print(f"⚠️  警告: 在 {input_folder} 中没有找到 .md 文件。")
        sys.exit(0)

    print(f"📂 正在处理文件夹: {input_folder}")
    print(f"📄 发现 {len(md_files)} 个 Markdown 文件，准备合并...")

    # 3. 准备输出目录 (如果输出目录的父文件夹不存在，则创建它)
    if not output_file.parent.exists():
        try:
            output_file.parent.mkdir(parents=True, exist_ok=True)
            print(f"📁 已创建输出目录: {output_file.parent}")
        except Exception as e:
            print(f"❌ 无法创建输出目录: {e}")
            sys.exit(1)

    # 4. 开始合并写入
    try:
        # 使用 utf-8 编码打开文件，确保兼容中文
        with open(output_file, 'w', encoding='utf-8') as outfile:
            for index, md_file in enumerate(md_files):
                print(f"   -> 正在合并: {md_file.name}")
                
                # 读取原始文件内容，不进行任何 strip() 操作，严格保留原始内容
                try:
                    content = md_file.read_text(encoding='utf-8')
                except UnicodeDecodeError:
                    # 如果 utf-8 失败，尝试常见的 latin-1 或报错
                    print(f"❌ 读取文件 {md_file.name} 失败，可能是编码问题。建议统一为 UTF-8。")
                    sys.exit(1)
                
                outfile.write(content)

                # 需求：不同文件内容之间留一个空行
                # 逻辑：如果不是最后一个文件，则写入分隔符
                if index < len(md_files) - 1:
                    # 写入两个换行符：一个结束当前行（如果原文件没换行），一个作为空行
                    # 注意：如果原文件末尾已经有换行，这里可能会多出空行，
                    # 但为了严格遵守"不增删修改文字"且保证"之间有空行"，写入 \n\n 是最稳妥的物理隔离。
                    outfile.write("\n\n")

        print("-" * 30)
        print(f"✅ 合并成功！")
        print(f"💾 输出文件: {output_file.absolute()}")

    except IOError as e:
        print(f"❌ 写入文件时发生错误: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ 发生未知错误: {e}")
        sys.exit(1)

def main():
    parser = setup_argparse()
    args = parser.parse_args()

    input_folder = Path(args.folder)
    output_file = Path(args.output)

    merge_markdown_files(input_folder, output_file)

if __name__ == "__main__":
    main()