# data = 'asddafadf'
# count = 0
# for x in data:
#     count += 1 
# print(count)

# #define 函数
# def say_hi():
#     print('i am black house')
# #必须调用函数
# say_hi()

# # #传入参数
# # def add(x,y):
# #     result = x + y
# #     print(f'{x}+{y} result is : {result}')

# add(5,6)

# def check(t):
#     print('welcome')
#     if t <= 37.5:
#         print(f'ok,{t} please')
#     else:
#         print(f'no,{t}9 far away')

# check(38)

# #return
# def add(a,b):
#     result = a + b
#     return result
# #'over'不执行
#     print('over')
# r = add (5,6)
# print(r)

# def check_age(age):
#     if age > 18:
#         return 'success'
#     else:
#         return None

# result = check_age(16)

# if not result:
#     print('not in')

# name = None

# def add(x,y):
#     result = x + y
#     print(f'result is {result}')
#     return result
# #返回了函数中的print↑和return的返回值的print↓
# a = add(5,6)
# print(a)

# def func_b():
#     print('---2---')
# def func_a():
#     print('---1---')
#     func_b()
#     print('---3---')

# func_a()

#局部变量 作用与函数体的内部
# def testA():
#     num = 100
#     print(num)
# testA()
# #无法print(num)
# print(num)

#全局变量，函数体内和体外都能够生效的变量
#很简单，将“变量定义在函数外面”
# num = 200
# def test_a():
#     print(f"test_a:{num}")
# def test_b():
#     print(f'test_b:{num}')

# test_a()
# test_b()
# print(num)

# num = 200
# def test_a():
#     print(f"test_a:{num}")
# def test_b():
#     num = 500 #又变成了局部变量
#     print(f'test_b:{num}')

# test_a()
# test_b()
# print(num)

# num = 200
# def test_a():
#     print(f"test_a:{num}")
# def test_b():
#     global num #设置内部定义的变量为全局变量
#     num = 500 
#     print(f'test_b:{num}')

# test_a()
# test_b()
# print(num)

# money = 5000000
# name = None

# name = input('name please: ')
# def query(show_header):
#     if show_header:
#         print('check')
#     print(f'{name},your monry:{money}yuan')
# def saving(num):
#     global money
#     money += num
#     print('saving')
#     print(f'{name}you save {num} is success')

#     query(False)
# def get_money(num):
#     global money
#     money -= num
#     print(f'{name} you take {num}yuan')
#     query(False)
# def main():


# while Ture:
#     keyboard_input = main()
#     if keyboard_input == '1'
#     query(Ture)

# def list_while_func():
#     my_list = ["aaa","bbb",'ccc']
#     index = 0
#     while index < len(my_list):
#         element = my_list[index]
#         print(f'element {element}')
#         index += 1
# list_while_func()


# def list_for_func():
#     my_list = [1,2,3,4,5]
#     for element in my_list:
#         print(f'list have: {element}')

# list_for_func()

# num = [1,2,3,4,5,6,7,8,9,10]
# element = 0
# even_element = []

# while element < len(num):
#     if num[element] % 2 == 0:
#         even_element.append(num[element])
#     element += 1
# print(f'偶数列表是: {even_element}')

# num = [1,2,3,4,5,6,7,8,9,10]
# even_element = []
# for x in num:
#     if x % 2 == 0:
#         even_element.append(x)
# print(f'偶数列表是: {even_element}')

info_dict ={
    'aaa':{
        'aaaA':"aaAA"
        ''
    },
    'bbb':{},
    'ccc':{},
    'ddd':{}

}



