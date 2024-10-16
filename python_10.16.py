# def user_info(name,age,gender):
#     print(f'姓名是： {name},年龄是: {age}, 性别是: {gender}')
# user_info(name='Any',age=20,gender='男')

def test_func(computer):
    result = computer(1,2)
    print(f'type{type(computer)}')
    print(f'{result}')

def computer(x,y):
    return x + y

test_func(computer)

def add(x,y):
    return x + y

test_func(add)