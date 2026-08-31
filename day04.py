nums = [1,2,3,4,5]
fruits = ["苹果","香蕉","橘子"]
mix = [1,"hi",True]
print(nums)
print(fruits)
print(mix)

# 索引是列表中的某个位置，切片是区间
nums = [10,20,30,40,50]
print(nums[0])   # 索引从0开始，nums[0]表示第一个元素
print(nums[-1])  # 负数索引表示从后往前数，-1表示最后一个元素
print(nums[1:4]) # 从索引1到索引4之前
print(nums[:2])  # 从开头到索引2之前
print(nums[::2]) # 步长为2，表示每隔一个元素取一个元素
print(nums[::-1]) # 步长为-1，表示倒序取元素

nums = [1,2,3]
nums[1] = 99
print(nums)

# 加减元素
""" append(x) 在列表末尾添加一个元素x

    insert(i,x) 在索引i的位置插入一个元素x
    extend(iterable) 在列表末尾一次性追加另一个可迭代对象中的多个值
    remove(x) 删除列表中值为x的第一个元素
    pop([i]) 删除列表中索引为i的元素，并返回该元素的值，若不指定索引，则删除并返回最后一个元素
    clear() 清空列表
"""

nums = [1,2,3]
nums.append(4)
nums.append([5,6])
print(nums)

nums = [1,2,3]
nums.insert(1,99)
nums.extend([7,8])
print(nums)

my_pocket = []
my_pocket.append("肥嘟嘟佐卫门")
print(my_pocket)

"""pop()方法可以删除列表中的元素，并且返回该元素的值。若不指定索引，则默认删除最后一个元素。
remove()方法可以删除列表中指定值的第一个元素，如果该值不存在，则会抛出ValueError异常。clear()方法可以清空列表中的所有元素。
del语句可以删除列表中的指定元素或整个列表，如果指定的索引不存在，则会抛出IndexError异常。
"""

nums = [1,2,3,4,5]
nums.pop()  # 删除最后一个元素
x = nums.pop(0)  # 删除索引为0的元素，并返回该元素的值
nums.remove(3)  # 删除值为3的第一个元素
del nums[1]  # 删除索引为1的元素
nums.clear()  # 清空列表
print(nums)
print(x)

# 查看和统计:len/in/count/index
nums = [1,2,3,4,5]
print(len(nums))  # 获取列表长度
print(nums.count(3))  # 统计值为3的元素个数
print(3 in nums)  # 判断值为3的元素是否存在
print(nums.index(4))  # 获取值为4的元素的索引

# 遍历列表
fruits = ["苹果","香蕉","橘子"]
for f in fruits:
    print(f)
for i in range(len(fruits)):  # range(len(fruits))表示从0到列表长度-1的整数序列
    print(i,fruits[i])

scores = [78,85,92,67,88]
scores.append(90)
scores.insert(1,80)
print(scores)
scores.pop()
scores.remove(67)
print(scores)

print(scores)
for s in scores:
    if s >= 60:
        print(f"及格：{s}")
    else:
        print(f"不及格：{s}")

average = sum(scores)/len(scores)
print(f"平均分：{average}")

shopping_list = ["水","面包"]
shopping_list.append("牛奶")
print("面包" in shopping_list)

