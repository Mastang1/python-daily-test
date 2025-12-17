# -*- coding: utf-8 -*-

# 1. 最基本的 %()s 字典替换
template = "你好，%(name)s！你是第%(rank)d位访客，今天是%(date)s。"
data = {
    "name": "张三",
    "rank": 12345,
    "date": "2025-12-10"
}

result = template % data
print(result)
# 输出：你好，张三！你是第12345位访客，今天是2025-12-10。