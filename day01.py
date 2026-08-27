# Day 01: 打印输出、变量、字符串拼接
# 目标：用变量保存个人信息并输出
print("Hello,我要转行做Python开发了!")
name = input("请输入你的名字：")
age = int(input("请输入你的年龄："))
city = input("请输入你所在的城市：")
target_salary = int(input("请输入你的目标薪资："))

# 字符串拼接写法
# print("我叫" + name + ", 今年" +str(age) + "岁, 在" + city + ", 我的目标薪资是" + str(target_salary) + "元/月")

# f-string写法
print(f"我叫{name}, 今年{age}岁, 在{city}, 我的目标薪资是{target_salary}元/月")
print("--- 个人信息 ---")
print(f"姓名：{name}")
print(f"年龄：{age}")
print(f"城市：{city}")
print(f"目标薪资：{target_salary} 元/月")
name = input("名字：")
age = int(input("年龄："))
city = input("城市：")
salary = int(input("目标薪资："))

print(f"{name}，{age}岁，在{city}，目标薪资{salary}元/月")