import argparse

'''
# 创建一个ArgumentParser对象
parser = argparse.ArgumentParser(description='dfdf')
# 添加一个位置参数
# parser.add_argument('name',type=str, help='name')
# parser.add_argument('color',type=str, help='like color')
# 添加一个可选参数
parser.add_argument('-a', '--age', type=int, default=18, help='your age')
# 解析命令行输入
args = parser.parse_args()
print(args.age)
'''


# for testing a group of argument
parser = argparse.ArgumentParser(description='dfdf')
execute_group = parser.add_argument_group('execute time')
execute_group.add_argument('-b', '--begin', type=str, help='input a begin time to start executing')
execute_group.add_argument('-e', '--end', type=str, help='input a end time to start executing')

#test mutex
group = parser.add_mutually_exclusive_group()  # 2
group.add_argument('--foo', action='store_true', help='foo help')  # 3
group.add_argument('--bar', action='store_true', help='bar help')  # 4


args = parser.parse_args()

print(args)


