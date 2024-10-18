class Student: #定义！类！
    name = None
    age = None #变量，定义类的！属性！-----成员变量

    def say_hi(self):
        print(f'Hi,大家好，我是{self.name}') #函数，定义类的！行为！（动作？）-----成员方法
    def say_hi2(self,msg):
        print(f'大家好，我是{self.name},{msg}')

stu = Student()
stu.name = 'zhoujielun'
stu.say_hi()

stu2 = Student()
stu2.name = 'linjunjie'
stu2.say_hi2('666')   

