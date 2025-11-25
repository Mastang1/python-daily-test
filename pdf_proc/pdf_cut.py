#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import pikepdf
import os

def split_pdf(input_file, ranges):
    print(f"[INFO] 打开 PDF：{input_file}")
    pdf = pikepdf.open(input_file)
    total_pages = len(pdf.pages)
    print(f"[INFO] 总页数：{total_pages}")

    basename = os.path.splitext(os.path.basename(input_file))[0]

    for idx, r in enumerate(ranges, 1):
        start, end = r

        if start < 1 or end > total_pages or start > end:
            print(f"[WARN] 跳过无效区间：{start}-{end}")
            continue

        print(f"[INFO] 分割区间：{start} → {end}")

        new_pdf = pikepdf.Pdf.new()
        # 页码从 0 开始
        for p in range(start - 1, end):
            new_pdf.pages.append(pdf.pages[p])

        outname = f"{basename}_{start}-{end}.pdf"
        new_pdf.save(outname)

        print(f"[DONE] 已生成：{outname}")

    print("[FINISH] 所有任务完成！")


def parse_range(s):
    try:
        parts = s.split("-")
        if len(parts) != 2:
            raise ValueError
        start = int(parts[0])
        end = int(parts[1])
        return (start, end)
    except:
        raise argparse.ArgumentTypeError(f"区间格式错误：{s}（正确格式：3-10）")


def main():
    parser = argparse.ArgumentParser(
        description="基于 pikepdf 的 PDF 分割工具（保持可复制文本）。"
    )
    parser.add_argument("input", help="输入 PDF 文件")
    parser.add_argument(
        "ranges",
        nargs="+",
        type=parse_range,
        help="要分割的页码区间，如：3-10 11-20"
    )

    args = parser.parse_args()
    split_pdf(args.input, args.ranges)


if __name__ == "__main__":
    main()
