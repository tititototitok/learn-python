s = "Hello python"

print(s[0])  # H(第一个字符)
print(s[-1]) # n(最后一个字符)
print(s[1:4]) # ell(从索引1到索引4之前)
print(s[6:]) # python(从索引6到结尾)
print(s[:5]) # Hello(从开头到索引5之前)
print(s[::2]) # Hlo yhn(步长为2，表示每隔一个字符取一个字符)
print(s[::-1]) # nohtyp olleH(步长为-1，表示倒序取字符)

# 字符串是不可变的类型，不能直接修改字符串中的字符

# 要改只能重新赋值
s = "h" + s[1:] # 将第一个字符改为小写 'h'
print(s) # hello python

text = "  hello python  "

print(text.strip())      # "hello python"（去掉两头空格）
print(text.lstrip())     # "hello python  "（只去左边）
print(text.rstrip())     # "  hello python"（只去右边）

print(text.lower())       # "  hello python  "（全小写）
print(text.upper())       # "  HELLO PYTHON  "（全大写）

print(text.replace("python", "world"))  # "  hello world  "（替换）

print(len(text))          # 16（长度，包括空格）

line = "hello,python,world"
print(line.split(","))  # ['hello', 'python', 'world']（变成列表了）

words = ["hello", "python", "world"]
print(" ".join(words))  # "hello python world"（列表变成字符串了
""" 字符串.split(分隔符)
分隔符.join(可迭代对象，通常是列表)
用什么分隔符,就切或者连接成什么样子
"""

filename = "day05.py"

print(filename.startswith("day"))  # True（判断是否以day开头）
print(filename.endswith(".py"))    # True（判断是否以.py结尾）

s = "hello python"
print(s.find("python"))  # 6（返回找到的起始索引，找不到返回-1）
print("python" in s)  # True（判断是否包含python）

# 元组(tuple)是不可变的序列类型，使用小括号()表示
t = (1, 2, 3)
print(t[0])  # 1（索引访问）
print(t[1:3])  # (2, 3)（切片访问）
# 切片中结束索引可以超过元组的长度，返回的结果不会报错，而是返回到元组的最后一个元素

# 函数返回多个值时，Python实际上是返回了一个元组
def get_point():
    return (3, 5)

x, y = get_point()  # 元组拆包
print(x, y)  # 3 5

# def是自定义一个函数
# print 是"打印出来给人看的"，return 是"把结果交出去给代码用的"。

for i in range(1, 6):
    print(i)  # 1 2 3 4 5
r = range(1, 6)
nums = list(range(1, 6))      # [1, 2, 3, 4, 5]
print(nums)
s = ",".join(str(n) for n in nums)
print(s)                       # "1,2,3,4,5"

# range 只能生成整数
r = range(1, 6)        # 1,2,3,4,5
print(list(r))          # [1, 2, 3, 4, 5]

# 转成列表看结果，方便理解
print(list(range(10)))           # [0,1,2,3,4,5,6,7,8,9]
print(list(range(0, 10, 2)))     # [0,2,4,6,8]
print(list(range(5, 0, -1)))     # [5,4,3,2,1]

# 练习1：字符串切片
s = "Hello, Python World!"
print(s[7:13])          # 取出 "Python"
print(s[::-1])           # 反转整个字符串

# 练习2：strip + split
line = "  苹果,香蕉,橙子  "
clean = line.strip()
fruits = clean.split(",")
print(fruits)

# 练习3：join 拼回去
joined = " | ".join(fruits)
print(joined)

# 练习4：用户输入处理（模拟）
user_input = "  LU BEN WEI  "
print(user_input.strip().lower())      # 去空格转小写

# 练习5：元组
point = (10, 20)
print(f"坐标：({point[0]}, {point[1]})")
print(f"坐标：{point}")

point = (10, 20)

# 明确控制
print(f"x={point[0]}, y={point[1]}")

# 直接放元组
print(f"point={point}")

x, y = point
print(f"坐标: ({x}, {y})")

# 练习6：range 转列表
print(list(range(1, 11)))              # 1到10
print(list(range(0, 21, 2)))           # 0到20的偶数


# 元组解包
point = (10, 20)
x, y = point
print(f"坐标: ({x}, {y})")