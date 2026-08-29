count =1

while count <= 5:
    print(count)
    count += 1

for i in range(1,6):
    print(i)

running = True

while running:
    print("循环中")
    running = False

#布尔值就是True和False
#代码运行逻辑就是判断真假之后再运行

age = 27
city = "嘻嘻"

if age >= 18 or city == "西安":
    print("成年且在西安")

# 用 input 控制
answer = ""
while answer != "quit":
    answer = input("输入 quit 退出：")
