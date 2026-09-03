r = int(input("请输入圆的半径: "))
def calc_area(r):
    """计算圆的面积"""
    import math
    return math.pi * r ** 2
print(calc_area(r))

def calc_area(r):
    """计算圆的面积"""
    return 3.14 * r ** 2
print(calc_area(3))

def 函数名(参数):
    """函数的说明文档"""
    函数体
    return 返回值 # 可以没有 return

def greet(name):
    """打印问候语"""
    print(f"Hello, {name}!")
greet("Alice")

def add(a, b):
    return a + b

result = add(3, 5)
print(result)        # 8

def say_hi():
    print("hi")

x = say_hi()
print(x)            # hi 然后 None

def divide(a, b):
    return a / b

print(divide(10, 2))    # 5.0

# 默认参数（有默认值，可传可不传）, 赋值了就不需要传参了
def greet(name, greeting="你好"):
    print(f"{greeting},{name}!")

greet("卢本伟")              # 你好，卢本伟！
greet("卢本伟", "早上好")     # 早上好，卢本伟！

# 默认参数必须放在非默认参数的后面，否则会报错
def greet(name, greeting="你好"):   # ✅ 正确
    pass
# def greet(greeting="你好", name):   # ❌ 报错



# 变量作用域
def test():
    x = 10  # 局部变量
    
test()
print(x)

# 练习1：定义函数is_even，判断一个数是否为偶数，如果是偶数返回True，否则返回False。
def is_even(num):
    """判断一个数是否为偶数"""
    return num % 2 == 0

print(is_even(4))  # True
print(is_even(3))  # False

# 练习2：定义函数max_of_two(a, b), 返回两个数中较大的一个。
def max_of_two(a, b):
    """返回两个数中较大的一个"""
    return a if a > b else b

print(max_of_two(4, 5))  # 5
print(max_of_two(10, 3))  # 10

# 练习3：定义函数great（name,greeting="你好"），打印问候语
def greet(name, greeting="你好"):
    """打印问候语"""
    print(f"{greeting}, {name}!")

greet("卢本伟")
greet("卢本伟", "早上好")

# 练习4：定义函数calculate(a, b, op="+")，根据参数op的值进行加减乘除运算，返回结果。
def calculate(a, b, op="+"):
    """根据参数op的值进行加减乘除运算，返回结果"""
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b
    else:
        raise ValueError("不支持的运算符")

print(calculate(10, 3))        # 13
print(calculate(10, 3, "-"))   # 7
print(calculate(10, 3, "*"))   # 30
print(calculate(10, 3, "/"))   # 3.3333333333333335
try:
    print(calculate(10, 3, "%"))   # ValueError: 不支持的运算符
except ValueError as e:
    print(e)

# 练习5：用练习1的is_even,打印1~10里的所有偶数
for i in range(1, 11):
    if is_even(i):
        print(i, end=" ")  # 2 4 6 8 10

# 这里的end=" "表示打印时不换行，而是用空格分隔，引号里可以是任何字符，比如end=","表示用逗号分隔，end="\n"表示换行，end=""表示不换行也不分隔。