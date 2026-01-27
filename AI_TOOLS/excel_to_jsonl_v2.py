import argparse
import pandas as pd
import json
import os
import sys
from datetime import datetime

def parse_args():
    # 定义帮助信息的示例文本
    example_text = '''使用示例 (Examples):

  1. 最简模式 (读取第一个Sheet，输出到output.jsonl):
     python excel_to_jsonl.py -i data.xlsx -o output.jsonl

  2. 指定Sheet名称 (读取名为 'FAQ' 的Sheet):
     python excel_to_jsonl.py -i data.xlsx -s "FAQ" -o output.jsonl

  3. 清洗换行符 (将单元格内的换行符替换为空格):
     python excel_to_jsonl.py -i data.xlsx -o output.jsonl --clean-newlines
    '''

    parser = argparse.ArgumentParser(
        description="🚀 Excel 转 AI 训练/识别用 JSONL 工具",
        epilog=example_text,
        formatter_class=argparse.RawTextHelpFormatter, # 关键：保留示例文本的换行格式
        add_help=True # 默认开启 -h/--help
    )

    parser.add_argument(
        '-i', '--input', 
        required=True, 
        metavar='FILE',
        help="[必填] 输入的Excel文件路径 (.xls 或 .xlsx)"
    )
    parser.add_argument(
        '-o', '--output', 
        required=True, 
        metavar='FILE',
        help="[必填] 输出的JSONL文件路径"
    )
    parser.add_argument(
        '-s', '--sheet', 
        required=False, 
        default=0,
        metavar='NAME_OR_INDEX',
        help="[可选] 指定Sheet名称或索引 (默认读取第1个Sheet)"
    )
    parser.add_argument(
        '--clean-newlines',
        action='store_true',
        help="[可选] 开启开关：将单元格内的软换行符由 \\n 替换为空格"
    )

    return parser.parse_args()

def json_serial(obj):
    """处理JSON默认不支持的类型 (如日期)"""
    if isinstance(obj, (datetime, pd.Timestamp)):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} not serializable")

def main():
    # 如果用户没有输入任何参数，直接打印帮助信息并退出
    if len(sys.argv) == 1:
        # 这里模拟调用了 -h
        os.system(f"python {sys.argv[0]} -h")
        sys.exit(0)

    args = parse_args()

    # --- 以下逻辑保持不变 ---
    if not os.path.exists(args.input):
        print(f"❌ 错误: 输入文件 '{args.input}' 不存在。")
        sys.exit(1)

    print(f"🔄 正在读取 Excel: {args.input} ...")

    try:
        df = pd.read_excel(args.input, sheet_name=args.sheet)
        df = df.fillna("")
        df.columns = df.columns.astype(str).str.replace('\n', ' ', regex=False).str.strip()

        record_count = 0
        with open(args.output, 'w', encoding='utf-8') as f:
            records = df.to_dict(orient='records')
            
            for row in records:
                clean_row = {}
                for k, v in row.items():
                    if args.clean_newlines and isinstance(v, str):
                        v = v.replace('\n', ' ').replace('\r', '')
                    if isinstance(v, str):
                        v = v.strip()
                    clean_row[k] = v
                
                f.write(json.dumps(clean_row, ensure_ascii=False, default=json_serial) + '\n')
                record_count += 1

        print(f"✅ 转换成功!")
        print(f"📂 输出文件: {args.output}")
        print(f"📊 处理行数: {record_count}")

    except ValueError:
        print(f"❌ 错误: 无法找到指定的 Sheet '{args.sheet}'。请检查名称是否正确。")
    except Exception as e:
        print(f"❌ 发生未预期的错误: {str(e)}")

if __name__ == "__main__":
    main()