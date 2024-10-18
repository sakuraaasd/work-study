#构造方法 __init__

class Student:
    # name = None
    # age = None
    # tel = None

    def __init__(self,name,age,tel):
        self.name  = name #在!成员方法!中访问!成员变量!就需要前面 + self
        self.age = age
        self.tel = tel
        print('Student类创建了一个对象的类')

stu = Student('zhoujielun',31,'1850006666')
print(stu.name)
print(stu.age)
print(stu.tel)

stu2 = Student('linjunjie',30,'13999020202')
print(stu2.name)
print(stu2.age)
print(stu2.tel)



