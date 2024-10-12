import argparse
 
# 定义一个补全的可能选项列表
completion_options = ['apple', 'banana', 'cherry']
 
# 创建ArgumentParser对象
parser = argparse.ArgumentParser()
# 补全函数
def completer(prefix, parsed_args, **kwargs):
    return [option for option in completion_options if option.startswith(prefix)] 
# 添加一个参数，并设置补全函数
parser.add_argument('fruit', type=str, choices=completion_options, completer=completer)
 

 
# 解析命令行参数
args = parser.parse_args()
 
# 使用参数
print(f"Selected fruit: {args.fruit}")