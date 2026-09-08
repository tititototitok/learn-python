import json
from datetime import datetime

"""
get_info(self) 叫实例方法，调用时是 s1.get_info(),Python 自动把 s1 传给 self。

@classmethod 叫类方法，调用时不用创建对象，直接用类名调用,常用来做"从别的数据格式创建对象
cls和self均为约定俗成的词汇,cls是类方法里接收"类本身"的参数名,第一个参数叫 self,代表"这个对象自己"
Tab:整体向右缩进

Shift + Tab:整体向左缩进

右下角显示 空格:4.确认是 4 空格缩进
"""

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def to_dict(self):
        return {"name": self.name, "score": self.score}



    @classmethod
    def from_dict(cls, d):
        return cls(d["name"], d["score"])
# cls是类（我要套这个公式了），d是字典（把d套到公式里）

    def get_info(self):
        return f"{self.name}: {self.score}"

    def is_pass(self):
        return self.score >= 60


class StudentManager:
    def __init__(self):
        self.students = []

    def add(self, name, score):
        self.students.append(Student(name, score))

    def show_all(self):
        if not self.students:
            print("暂无学生")
            return
        for s in self.students:
            status = "及格" if s.is_pass() else "不及格"
            print(f"{s.get_info()} ({status})")

    def find(self, name):
        for s in self.students:
            if s.name == name:
                print(f"{s.get_info()}")
                return
        print(f"没找到 {name}")

    def delete(self, name):
        for s in self.students:
            if s.name == name:
                self.students.remove(s)
                print(f"{name} 已删除")
                return
        print(f"没找到 {name}")

    def average(self):
        if not self.students:
            print("暂无学生")
            return
        total = sum(s.score for s in self.students)
        avg = total / len(self.students)
        print(f"平均分: {avg:.1f}")

    def save(self, filename="students.json"):
        data = [s.to_dict() for s in self.students]
        with open(filename, "w", encoding="utf-8")as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print("已保存到文件")
# txt要自己 split(",") 解析。JSON 不用，Python 直接认识，一行代码读回来就是列表字典
# data：要存的 Python 数据（列表/字典）
# f：文件对象
# ensure_ascii=False：让中文正常显示，不然会变成 \u5e10...
# indent=2：格式化缩进，看着好看

    def load(self,filename="students.json"):
        try:
            with open(filename, "r", encoding="utf-8")as f:
                data =json.load(f)
            self.students = [Student.from_dict(d) for d in data]
            print("已从文件加载")
        except FileNotFoundError:
            print("文件不存在，从空列表开始")


def show_menu():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:&S")
    print(f"\n=== 学生成绩管理 ({now}) ===")
    print("1. 添加学生")
    print("2. 查看所有")
    print("3. 查询成绩")
    print("4. 删除学生")
    print("5. 算平均分")
    print("6. 保存")
    print("7. 退出")

def main():
    manager = StudentManager()
    manager.load()

    while True:
        show_menu()
        choice = input("选择操作(1-7): ")

        if choice == "1":
            name = input("输入学生姓名：").strip()
            if not name:
                print("姓名不能为空")
                continue
            # continue 用在循环里，意思是：跳过这次循环剩下的部分，直接回到循环顶部开始下一次。
            try:
                score = int(input("输入成绩："))
            except ValueError:
                print("成绩必须是整数")
                continue
            manager.add(name, score)
            print(f"{name} 添加成功")

        elif choice == "2":
            manager.show_all()

        elif choice == "3":
            name = input("输入要查的学生姓名：")
            manager.find(name)

        elif choice == "4":
            name = input("输入要删除的学生姓名：")
            manager.delete(name)

        elif choice == "5":
            manager.average()

        elif choice == "6":
            manager.save()

        elif choice == "7":
            manager.save()
            print("再见")
            break

        else:
            print("输入无效")


main()