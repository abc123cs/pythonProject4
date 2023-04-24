from file_manager import FileManager
from student import Student


class StudentManager:
    def __init__(self):
        self.file_manager = FileManager("data.txt")
        self.students = self.file_manager.read_data()

    def register(self):
        name = input("请输入姓名：")
        id = input("请输入学号：")
        gender = input("请输入性别：")
        score = input("请输入成绩：")
        student = Student(name, id, gender, score)
        self.students.append(student)
        self.file_manager.save_data(self.students)
        print("注册成功！")

    def login(self):
        id = input("请输入学号：")
        found = False
        for student in self.students:
            if student.id == id:
                found = True
                print("登录成功！")
                return student
        if not found:
            print("学号不存在！")

    def add(self):
        name = input("请输入姓名：")
        id = input("请输入学号：")
        gender = input("请输入性别：")
        score = input("请输入成绩：")
        student = Student(name, id, gender, score)
        self.students.append(student)
        self.file_manager.save_data(self.students)
        print("添加成功！")

    def delete(self):
        id = input("请输入学号：")
        for student in self.students:
            if student.id == id:
                self.students.remove(student)
                self.file_manager.save_data(self.students)
                print("删除成功！")
                return
        print("学号不存在！")

    def view(self):
        print("{:<10}{:<10}{:<10}{:<10}".format("姓名", "学号", "性别", "成绩"))
        for student in self.students:
            print("{:<10}{:<10}{:<10}{:<10}".format(student.name, student.id, student.gender, student.score))

    def modify(self):
        id = input("请输入学号：")
        found = False
        for student in self.students:
            if student.id == id:
                found = True
                name = input("请输入姓名：")
                gender = input("请输入性别：")
                score = input("请输入成绩：")
                student.name = name
                student.gender = gender
                student.score = score
                self.file_manager.save_data(self.students)
                print("修改成功！")
        if not found:
            print("学号不存在！")