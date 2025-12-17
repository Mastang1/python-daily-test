import re
import sys
from bs4 import BeautifulSoup
import openpyxl

# Excel 不允许的字符过滤
_ILLEGAL_CHARS_RE = re.compile(r"[\x00-\x08\x0B-\x0C\x0E-\x1F]")
def clean_text(s):
    if not isinstance(s, str):
        return s
    return _ILLEGAL_CHARS_RE.sub("", s)

# 新的时间格式：20251205_11_44_55
TIME_RE = re.compile(r"\d{8}_\d{2}_\d{2}_\d{2}")

def parse_html_to_excel(input_html, output_excel="output.xlsx"):
    with open(input_html, "r", encoding="utf-8") as f:
        html_text = f.read()

    soup = BeautifulSoup(html_text, "html.parser")
    text = soup.get_text("\n")
    lines = text.splitlines()

    testcases = []
    current_case = None
    log_collecting = False
    log_buffer = []
    wait_for_time = False     # 标记：刚遇到 tcfTcs_xxx，下一行中寻找时间

    for line in lines:
        line = line.strip()

        # -----------------------------
        # 1. 捕获 tcfTcs_xxx
        # -----------------------------
        if line.startswith("tcfTcs_"):
            if current_case:
                current_case["log"] = "\n".join(log_buffer)
                testcases.append(current_case)
                log_buffer = []

            current_case = {
                "name": line,
                "time": "",
                "log": "",
                "result": ""
            }
            wait_for_time = True
            continue

        # -----------------------------
        # 2. 捕获时间格式：20251205_11_44_55
        # -----------------------------
        if wait_for_time and current_case:
            m = TIME_RE.search(line)
            if m:
                current_case["time"] = m.group(0)
                wait_for_time = False
        # 避免跨太多行
        if wait_for_time and line == "":
            # 空行也算过渡，但不取消 wait_for_time
            pass

        # -----------------------------
        # 3. 日志开始
        # -----------------------------
        if line.startswith("test begin >>>"):
            log_collecting = True
            continue

        # -----------------------------
        # 4. 日志结束
        # -----------------------------
        if line.startswith(">>> test end"):
            log_collecting = False
            continue

        # -----------------------------
        # 5. 收集日志内容
        # -----------------------------
        if log_collecting:
            log_buffer.append(line)

        # -----------------------------
        # 6. pass/fail 判断
        # -----------------------------
        if current_case and ("pass" in line.lower() or "fail" in line.lower()):
            if "pass" in line.lower():
                current_case["result"] = "pass"
            if "fail" in line.lower():
                current_case["result"] = "fail"

    # -----------------------------
    # 推入最后一个 case
    # -----------------------------
    if current_case:
        current_case["log"] = "\n".join(log_buffer)
        testcases.append(current_case)

    # -----------------------------
    # 写入 Excel
    # -----------------------------
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(["TestCase", "Time", "Log", "Result"])

    for tc in testcases:
        ws.append([
            clean_text(tc["name"]),
            clean_text(tc["time"]),
            clean_text(tc["log"]),
            clean_text(tc["result"])
        ])

    wb.save(output_excel)
    print(f"已生成：{output_excel}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python temp.py input.html [output.xlsx]")
    else:
        input_html = sys.argv[1]
        output_excel = sys.argv[2] if len(sys.argv) > 2 else "output.xlsx"
        parse_html_to_excel(input_html, output_excel)
