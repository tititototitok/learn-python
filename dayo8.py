# int 是整数没小数点，float 是小数有小数点。除法 / 永远出 float。
def add_student(students):
    name = input("请输入学生姓名：").strip()  # 去掉首尾空格
    if not name:
        print("姓名为空，已取消")
        return
    score = int(input("请输入学生成绩："))
    students.append({"name": name, "score": score})
    print(f"{name}添加成功")

def show_all(students):
    if not students:
        print("暂无学生信息")
        return
    for student in students:
        print(f"姓名: {student['name']}, 成绩: {student['score']}")

def find_student(students):
    name = input("请输入要查找的学生姓名：")
    for student in students:
        if student["name"] == name:
            print(f"姓名: {student['name']}, 成绩: {student['score']}")
            return
    print("未找到{name}")

def delete_student(students):
    name = input("请输入要删除的学生姓名：")
    for student in students:
        if student["name"] == name:
            students.remove(student)
            print(f"{name}删除成功")
            return
    print(f"未找到{name}")

def average_score(students):
    if not students:
        print("暂无学生,无法计算平均成绩")
        return
    total = sum(student["score"] for student in students)
    average = total / len(students)
    print(f"平均成绩: {average:.1f}")
# :.1f = 保留 1 位小数，四舍五入，.2f = 保留 2 位小数，四舍五入

def main():
    students = []
    while True:
        print("\n=== 学生管理系统 ===")
        print("1. 添加学生")
        print("2. 查看所有")
        print("3. 查询成绩")
        print("4. 删除学生")
        print("5. 计算平均成绩")
        print("6. 退出")
        choice = input("请输入操作编号: ")
        
        if choice == "1":
            add_student(students)
        elif choice == "2":
            show_all(students)
        elif choice == "3":
            find_student(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            average_score(students)
        elif choice == "6":
            print("退出系统")
            break
        else:
            print("无效的操作编号，请重新输入")

main()    # 现在，开始执行 main 函数。
