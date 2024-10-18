class Student:
    def __init__(self,name,age,add):
        self.name = name
        self.age = age
        self.add = add 
num = 10
for x in range(1,num+1):
    print(f'现在录入第{x}位学生信息,总共需要录入10位学生信息')
    name = input('请输入学生姓名：')
    age = input('请输入学生年龄：')
    add = input('请输入学生地址：')
    stu = Student(name,age,add)
    print(f'学生{x}信息录入完成，信息为【学生姓名：{stu.name},学生年龄:{stu.age},学生地址:{stu.add}】总共需要录入10位学生信息')
