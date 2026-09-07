def save_to_file(students):
    with open("students.txt", "w", encoding="utf-8") as f:
    # with open(...) as f: 里的 f 是“文件对象”的变量名，可以理解成：给打开的这个文件起个短名字，后面用 f 操作它。
    # 以文本写入方式打开，并且规定用 UTF-8 编码来存/读文字。计算机存文件底层是字节，文字要按规则转成字节，这个规则就是编码。utf-8 是一种能表示中文、英文、表情等很通用的编码。
        for s in students:
            f.write(f"{s["name"]},{s["score"]}\n")
            # \n 是换行符，表示写完一条学生信息后换行，下一条信息另起一行。
        print("保存成功")
        # for 和 while 都是循环，只是写法不同。for 专门用来遍历列表/字符串/范围等已知序列，while 用来按条件反复执行。

def load_from_file():
    students = []
    with open("students.txt", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()  # 去掉每行开头和结尾的空白符（包括换行符）
            name, score = line.split(",")  # 按逗号分割成两个部分
            students.append({"name": name, "score": int(score)})
    return students

students = [
    {"name": "卢本伟", "score": 88},
    {"name": "马飞飞", "score": 92},
    {"name": "大司马", "score": 100}
]

# 存到文件
save_to_file(students)

# 文件读取
loaded = load_from_file()

# 打印看看
print(loaded)