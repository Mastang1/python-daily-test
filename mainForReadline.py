import readline
import pdb
import inspect

# 自动补全的函数
def auto_complete(text, state):
    import sys
    lines = readline.get_line_buffer().split()
    if len(lines) > 1:
        # 假设只考虑单词的补全
        matches = [word for word in words if word.startswith(text)]
        if state < len(matches):
            return matches[state]
        else:
            return None
    else:
        return [word for word in words if word.startswith(text)][state]
 
# 假设这是我们要补全的词汇列表
words = ['apple', 'application', 'banana', 'bandwidth', 'bear']
 
# 设置自动补全的函数
readline.set_completer(auto_complete)
 
# 启动补全
readline.parse_and_bind('tab:complete')
 
# 用户输入
user_input = input("Enter a word: ")