class student:
    def __init__(self, name, score):
    # __init__ 两侧均为双下划线
        self.name = name
        self.score = score

    def get_info(self):
        return f"{self.name}: {self.score}"

    def is_pass(self):
        return self.score >= 60

s1 = student("卢本伟", 88)
s2 = student("马飞飞", 98)

print(s1.get_info())  # 卢本伟：88
print(s2.get_info())  # 马飞飞: 98
print(s1.is_pass())   # True

students = []
students.append(student("卢本伟", 88))
students.append(student("马飞飞", 98))
students.append(student("大司马", 95))

for s in students:
    print(s.get_info(), "及格"if s.is_pass() else "不及格")

