# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return f'Student类对象,name:{self.name},{self.age}'
#     # def __lt__(self.other):
#     #     return self.age < other.age
    
# stu = Student('zhoujielun',30)
# print(stu)
# print(str(stu))

#私有成员变量和私有成员方法的使用
#__名字前加双下划线，不能够直接调用
class Phone:
    #提供私有成员变量：__is_5g_enable
    __is_5g_enable = False

    #提供私有成员方法：__check_5g
    def __check_5g(self):
        if self.__is_5g_enable:
            print("5g is on")
        else:
            print('5g is off, use 4g')

    #提供公开成员方法：call_by_5g
    def call_by_5g(self):
        self.__check_5g()
        print('正在通话中') 
phone = Phone()
phone.call_by_5g()