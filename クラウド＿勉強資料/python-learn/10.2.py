
#单引号定义法
name = '黑马程序员'
print(type(name))
# 双行定义法
name = "黑马程序员"
print(type(name))
# 三引号定义法
name = """
我是
黑马
程序员
"""
print(type(name))

# 在字符串内包含双引号
name = '"黑马程序员"'
print(name)
# 在字符串内包含单引号
name = "'黑马程序员'"
print(name)
# 使用转义字符\解除引号的效用
name = "\"黑马程序员\""
print(name)
name = '\'黑马程序员\''
print(name)

name = '黑马程序员'
print(name)

# 字面量之间的拼接

print("学IT来黑马"+"月薪过万")

name = "黑马程序员"
address = "建材东路9号院"
print("我是："+name+",我的地址是："+address)

class_num = 57
avg_salary = 16781
message = 'python大数据学科，北京%s期，毕业平均工资：%s'%(class_num,avg_salary)
print(message)

name = "传智博客"
set_up_year = 2006
stock_price = 19.99
# f=format
print(f'我是{name},我成立于：{set_up_year}年,我今天的股价是：{stock_price}')

# 表达式 = 一条具有明确执行结果的代码语句
# 1+1 5*2 name = zhangsan age = 11+11

print("1*1的结果是：%d"%(1*1))
print(f"1*2的结果是：{1*2}")
print(f'字符串在Python中类型的名称是：{type("字符串")}')

print(f'公司：{"传智博客"}，股票代码：{"003032"},当前股价：{19.99}')
su = 1.2
day = 7
arrive = 71.63
print('每日增长系数是：%2.1f,经过%d天的增长后,股价达到了：%4.2f'%(su,day,arrive))

# 输入数字类型
# num = input("请告诉我你的银行卡密码：")
# num = int(num)
# print("你的银行卡密码的类型是：",type(num))

# user_name = input("您好：")
# user_type = input("您是尊贵的：")
# print("您好：",user_name,"您是尊贵的：",user_type,"用户，欢迎您的光临")

# 定义变量储存布尔类型的数据 字变量
bool_1 = True
bool_2 = False
print(f"bool_1变量的内容是：{bool_1},类型是：{type(bool_1)}")
print(f"bool_2变量的内容是：{bool_2},类型是：{type(bool_2)}")

#比较运算符的使用
# == , != , >, <, , >=, <=

num1 = 10
num2 = 10
print(f"10 == 10的结果是：{num1 == num2}")

num1 = 10
num2 = 15
print(f"10 != 15的结果是：{num1 != num2}")

name1 = "itcast"
name2 = "itheima"
print(f'itcast == itheima的结果是：{name1 == name2}')

# 演示大于小余，大于等于小于等于的比较运算
num1 = 10
num2 =5
print(f'10 > 5结果是：{num1 > num2}')

num1 = 10
num2 = 11
print(f"10>=11的结果是：{num1>=num2}")
print(f"10<=11的结果是：{num1<=num2}")

age = 10
# if age >= 18:
#     print("我已经成年了")
#     print("即将步入大学生活")
# print('时间过的真快啊')

# 演示练习题
# 获取键盘输入
# age =int(input(f"请输入您的年龄："))
# if age >= 18:
#     print("您已成年，游玩需要补票10元")
#
# print("祝您游戏愉快")

# if else

# age = int(input("请输入你的年龄："))
# if age >= 18:
#     print("您已成年需要买票10元")
# else:
#     print("您未成年，可以免费游玩")

# tall = int(input("请输入你的身高（cm）："))
# if tall >= 120:
#     print("您的身高超出120cm,需要购票10元")
# else:
#     print("您的身高未超出120cm,可以免费游玩")
# print("祝您游玩愉快")

# if int(input("请输入你的身高cm：")) <120:
#     print("身高小于120cm,可以免费")
# elif int(input("请输入你的VIP等级：")) > 3:
#     print("VIP级别大于3，可以免费")
# elif int(input('请告诉我今天几号：')) == 1:
#     print("今天是1号免费日，可以免费")
# else:
#     print("不好意思，条件都不满足需要买票10元")
# num = 10
# if int(input("请猜一个数字")) == num:
#     print("恭喜第一次就猜对了呢")
# elif int(input("猜错了，再猜一次：")) == num:
#     print("猜对了")
# elif int(input("猜错了，再猜一次：")) == num:
#     print("恭喜，最后一次机会，你猜对了")
# else:
#     print("Sorry,猜错了")

# 判断语句的嵌套使用（if语句）
"""
if int(input("你的身高是多少")) >120:
    print("身高超出限制，不可以免费")
    print("但是，如果VIP级别大于3,可以免费")
    if int(input('你的VIP级别是多少')) >3:
        print("恭喜你，VIP级别达标，可以免费")
    else:
        print("Sorry,你需要买票10元")
else:
    print("欢迎小朋友免费游玩")
"""
"""
age = 20
year = 1
level = 1
if age >= 18:
    print("您是成年人")
    if age <= 30:
        print('您的年龄达标了')
        if year >2:
            print("恭喜您，年龄和入职时间都达标，可以；领取礼物")
        elif level >3:
            print("恭喜您，年龄和级别达标，可以领取礼物")
        else:
            print('不好意思，尽管年龄达标，但是入职时间和级别都不达标')
    else:
        print('不好意思，年龄太大了')
else:
    print('不好意思，小朋友不可以领取。')
"""
# 构建一个最急的数字变量
import random
num = random.randint(1,10)

guess_num = int(input('输入你要猜测的数字:'))

# 通过if语句进行数字的猜测
if guess_num == num:
    print('恭喜，第一次就猜中了')
else:
    if guess_num > num:
        print('你猜测的数字大了')
    else:
        print('你猜测的数字小了')

    guess_num = int(input('第二次输入你要猜测的数字:'))

    if guess_num == num :
        print('恭喜，第二次猜中了')
    else:
        if guess_num > num:
            print('你猜测的数字大了')
        else:
            print('你猜测的数字小了')
        guess_num = int(input('第二次输入你要猜测的数字:'))
        if guess_num == num:
            print('第三次猜中了')
        else:
            print('三次机会用完了，没猜中。')






