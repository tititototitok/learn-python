# 1. while 计数
count =1
while count <= 5:
    print(count)
    count += 1

# range(起始值,结束值)函数是生成一个序列
# range(1,6) 生成一个从1到5的整数序列,python的设计结束值永远取不到
for i in range(1,6):
    print(i)

running = True

while running:
    print("循环中")
    running = False

# 布尔值就是True和False
# 代码运行逻辑就是判断真假之后再运行

age = 27
city = "嘻嘻"

if age >= 18 or city == "西安":
    print("成年且在西安")

# 用 input 控制
answer = ""
while answer != "quit":
    answer = input("输入 quit 退出：")

nums = [1, 2, 3, 4, 5]
print(nums[1:2])
print(nums[1])

for i in range(10,-2,-2):
    if i == 8:
        continue
    elif i == 0:
        break  
    print(i)

total = 0
for i in range(1, 101):
    total += i
print(total)

# %是取余数。i % 2 == 0表示i除以2的余数为0，即i是偶数
for i in range(1, 11):
    if i % 2 == 0:
        print(i)

# 练习：计算1-100之间所有奇数的和
total = 0
for i in range(1, 101):
    if i % 2 != 0:
        total += i
print(total)

# 倒计时
count = 5
while count > 0:
    print(count)
    count -= 1 

print("开始！")
