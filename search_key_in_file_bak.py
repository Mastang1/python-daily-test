def simple_search_tcf(file_path):
    """简化版的tcf@搜索函数"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                if 'tcfTcs_IPCS' in line:
                    tcf_pos = line.find('tcfTcs_IPCS_TS_7_TC_000_MngPolling')
                    result = line[tcf_pos:].strip()
                    print(f"行{line_num}: {result}")
    except FileNotFoundError:
        print(f"文件 '{file_path}' 不存在")

# 使用示例
if __name__ == "__main__":
    simple_search_tcf("C:\\tangyapeng\\docs\\StarGather\\report_gen_proj\\mculong-test-ipcs_20251014_09_25_37.html")