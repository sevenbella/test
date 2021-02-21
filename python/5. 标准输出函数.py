# 普通输出
number1 = 100
number2 = 200
number3 = 150
print(number1)

# \n 换行符
print('abc', end='')  # 该输出后面不换行  不备注“end = '' 时则为end值为默认状态-- end='\n' 会换行

print(100)


# 格式化输出  需要有一个格式
name = '司马'
age = 20
salary = 7786

#  写法1 格式：
my_format ='名字是%s，年龄是%d，工资是%.2f' % (name, age, salary)  # %为占位符
print(my_format)

# 写法2  该表达会有空格
print('名字是', name, '年龄是', age, '工资是', salary)

# 先生成字符串，后输出
print('名字是%s，年龄是%d，工资是%.2f' % (name, age, salary))
print('aaa' + 'bbb')  #表达式  该表达式最后输出结果为：aaabbb

# 输出%需为%%
print('占比为%d%%' % 87)

