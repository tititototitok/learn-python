# day 02: if/else/elif 条件判断
age=int(input("请输入你的年龄："))

if age >= 18:
    print("你已成年")
else:
    print("你未成年")
if age != 27:
    print("可以偷懒")
else:
    print("霎眼廿七岁时日无多放不敢偷懒")
target_salary = int(input("请输入你的目标薪资："))

if target_salary < 5000:
    print("可以先以入行为主(copilot吐槽目标过低)")
elif target_salary < 10000:
    print("比较现实，继续加油")
elif target_salary < 20000:
    print("有挑战，但可达")
else:
    print("目标很高，需要强技能支撑")


# 猜数字小游戏基础版
answer = 18
guess = int(input("猜一个整数："))

if guess == answer:
    print("恭喜你，猜对了")
elif guess > answer:
    print("猜大了")
else:
    print("猜小了")
