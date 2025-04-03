my_dict = {'name': '张三', 'age': 30, 'city': '北京'}

# 保持插入顺序（Python 3.7+保证字典有序）
result = ' '.join(f"{k} {v}" for k, v in my_dict.items())
# 输出: 'name=张三, age=30, city=北京'
print(result)