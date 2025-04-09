import os

# 设置环境变量（通常在外部设置，这里演示用）
os.environ['MY_FEATURE_FLAG'] = 'true'

# 读取环境变量进行分支控制
if os.getenv('MY_FEATURE_FLAG', 'false').lower() == 'true':
    print("启用新功能")
    # 执行新功能代码
else:
    print("使用旧功能")
    # 执行旧功能代码
