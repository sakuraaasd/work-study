name = 'Python'
age = 27
#打印 "我是Python，今年27岁了"
new_str = '我是' + name + "," + '今年' + str(age) + "岁了"
print(new_str)

new_str_1 = "我是{name},今年{age}岁了".format(
    name = 'aaaa' , age = 'bbbb'
)
print(new_str_1)

name1 = "abc"
age1 = '30'
new_str_2 = f"我是{name1},今年{age1}岁了"
print(new_str_2)

#str(['hellow','world'])
#print(str(['hellow','world']))

s2 = 'A new version of    python'
s2.split
result = s2.split()
print(result)