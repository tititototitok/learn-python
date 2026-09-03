# 字典(dict) + 集合(set)的使用
person = {
    "name": "卢本伟",
    "age": 27,
    "city": "西安"
}

print(person["name"])  # 卢本伟
print(person["age"])   # 27
print(person["city"])  # 西安

person = {"name": "卢本伟", "age": 27}

# 改
person["age"] = 28
print(person) #{"name": "卢本伟", "age": 28}

# 增(键不存在就自动新增)
person["salary"] = 8000
print(person)  #{"name": "卢本伟", "age": 28, "salary": 8000}

# 查(get,键不存在不会报错)
print(person.get("name"))  # 卢本伟
print(person.get("gender"))  # None
print(person.get("height",168))  # 168，键不存在时返回默认值

#  删
person.pop("salary")  # 删除键为"salary"的键值对
print(person)  #{"name": "卢本伟", "age": 28}

# 删全部
# person.clear()

# 字典的三种视图
person = {"name": "卢本伟", "age": 28, "city": "西安"}

print(person.keys())    # dict_keys(['name', 'age', 'city']) 所有键
print(person.values())  # dict_values(['卢本伟', 28, '西安']) 所有值
print(person.items())   # dict_items([('name', '卢本伟'), ('age', 28), ('city', '西安')]) 所有键值对

# 遍历字典
for key, value in person.items():
    print(f"{key}: {value}")

person = {"name": "卢本伟", "age": 27, "city": "西安"}

# 只遍历键(默认就是键)
for key in person:
    print(key)

# 只遍历值
for value in person.values():
    print(value)

# 同时遍历键和值
for key, value in person.items():
    print(key, value)

# 集合(set)的使用
# 集合是无序的、不可重复的数据集合
nums = {1, 2, 2, 3, 3, 4}
# 如果加一行unique = set(nums)，那么unique就是一个新的集合，里面的元素是nums去重后的结果，相当于把去重后的结果保留下来了
print(nums)  # {1, 2, 3, 4}，重复的元素会被自动去重

# 空集合不能写成 {}，因为 {} 是空字典的语法，空集合需要使用 set() 来创建
empty_set = set()

# 集合常用操作
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a & b)  # {3, 4}，交集
print(a | b)  # {1, 2, 3, 4, 5, 6}，并集
print(a - b)  # {1, 2}，差集
print(b - a)  # {5, 6}，差集
print(a ^ b)  # {1, 2, 5, 6}，对称差集

# 判断在不在
nums = {1, 2, 3}
print(2 in nums)  # True
print(4 in nums)  # False
# set判断in的时间复杂度是O(1)，而list判断in的时间复杂度是O(n)，所以set在判断元素是否存在时效率更高。

# 练习1：建一个学生字典，包含name/age/score，打印name和score
student = {"name": "卢本伟", "age": 20, "score": 90}
print(student["name"])  # 卢本伟
print(student["score"])  # 90

# 练习2：用 get 取 age， 取一个不存在的键"gender", 给默认值"未知"
print(student.get("age"))  # 20
print(student.get("gender", "未知"))  # 未知

# 练习3：新增键"city",值为"西安"，然后打印整个字典
student["city"] = "西安"
print(student)  # {'name': '卢本伟', 'age': 20, 'score': 90, 'city': '西安'}

# 练习4：用items()遍历字典，打印每个键值对
for key, value in student.items():
    print(key, value)

# 练习5：建一个列表有重复数字，用集合去重，打印结果
nums = [1, 2, 2, 3, 3, 4]
unique = set(nums)
print(unique)  # {1, 2, 3, 4}

# 练习6：两个集合，求交集、并集
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("交集", set1 & set2)  # {3, 4}，交集
print("并集", set1 | set2)  # {1, 2, 3, 4, 5, 6}，并集
