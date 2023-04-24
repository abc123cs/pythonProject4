user=['zhangkaipeng']
pwd=['123456']

def denglu():
    users = input("请输入您的用户名:")
    pwds = input("请输入您的密码:")
    if users in user and pwds in pwd:
        student()
    else:
        print("账号或密码不正确，请重新输入")
def zhuce():
    users=input("请输入您要注册的用户名:")
    pwds=input("请输入您要注册的密码:")
    user.append(users)
    pwd.append(pwds)
    print()
    print("注册成功!")
    print()

def dljiemian():

     while True:
            print("---------------------------")
            print("    学生管理系统登陆界面       ")
            print("                           ")
            print("        1:登   录           ")
            print("        2:注   册           ")
            print("        3:退   出           ")
            print("                           ")
            print("---------------------------")
            xx = input("请输入您的选择:")
            # 1.登录
            if xx == '1':
                denglu()
            elif xx == '2':
                # 2.注册
                zhuce()
            elif xx == '3':
                # 3.退出
                print()
                print("成功退出!")
                print()
                break
            else:
                print("输入错误，请重新输入")
class Student:
    def __init__(self, name, id, age):
            self.name = name
            self.id = id
            self.age = age
def showInfo():
    print("-" * 30)
    print("1.添加学生的信息")
    print("2.删除学生的信息")
    print("3.修改学生的信息")
    print("4.查询学生的信息")
    print("5.遍历学生的信息")
    print("6.退出系统")
    print("-" * 30)
class StudentManager:
   def __init__(self):
       self.student_list = []
#1.添加学生的信息
   def addNewStu(self):
     name = input("请输入学生的姓名：")
     id = input("请输入学生的学号：")
     age = input("请输入学生的年龄：")
     student = Student(name,id,age)
     self.student_list.append(student)
     print("添加成功")
#删除学生的信息
   def del_info(self):
     del_name = input("请输入需要删除的学生姓名：")

     for student in self.student_list:
        if del_name == student.name:
           self.student_list.remove(student)
           print("该学生信息成功删除")
           break

     print("该学生信息不存在，请重新操作！！！")
#修改的信息
   def modify_info(self):
      modify_name = input("请输入需要修改的学生姓名：")
      if (self.student_list.__len__() == 0):
          print("没有学生")
          return
      for student in self.student_list:
        if modify_name == student.name:
           student.id = input("请输入新的学号：")
           student.age = input("请输入新的年龄：")
           print("该学生信息成功修改")
           break
           print("该学生信息不存在，请重新操作!!!")
#查询学生的信息
   def search_info(self):
      search_name = input("请输入需要查询的学生姓名：")
      #todo
      if(self.student_list.__len__() == 0):
          print("没有学生")
          return

      for student in self.student_list:
        if search_name == student.name:
           print("查询到的学生信息如下-----------------")
           print(f"学生的姓名是{student.name},学生的学号是{student.id},学生的年龄是{student.age}")
           return

      print("对不起，该学生信息不存在，请重新操作！！！")
#5.遍历学生的信息
   def print_all(self):
     print('姓名\t学号\t年龄')
     for student in self.student_list:
        print(f"{student.name}\t{student.id}\t{student.age}")

def student():
    student_manager = StudentManager()
    while True:
      showInfo()
      key = int(input("请选择功能："))
      if key == 1:
        student_manager.addNewStu()
      elif key ==2:
        student_manager.del_info()
      elif key ==3:
        student_manager.modify_info()
      elif key ==4:
        student_manager.search_info()
      elif key ==5:
        student_manager.print_all()
      elif key ==6:
          exit_flag = input("您确定要退出系统吗？yes/no")
          if exit_flag == 'yes':
              print("成功退出学生管理系统！")
              break
          else:
              print("输入有误，请重新输入")
dljiemian()






