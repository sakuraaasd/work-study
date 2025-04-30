# 通过一个布尔类型的变量，做循环是否继续的标记

"""""
import random
num = random.randint(1,100)
count = 0
flag = True
while flag :
    guess_num = int(input('请输入你猜测的数字：'))
    count += 1
    if guess_num == num:
        print("猜中了")
        flag = False
    else:
        if guess_num > num:
            print("你猜的大了")
        else:
            print("你猜的小了")

print(f"你总共猜测了{count}次：")
"""

# while 的嵌套使用
# 外层 100天的控制
# 内层 每天都送10支花的控制

"""
i = 1
while i <= 100:
    print(f"今天是第{i}天，准备表白...")
    j = 1
    while j <=10 :
        print(f'送给小美第{j}支玫瑰花')
        j += 1
    print('小美，我喜欢你')
    i += 1
print(f'坚持到第{i-1}天，表白成功')

# print('Hello',end="")
# print('World',end="")

print("Hello Workd")
print('iteheima best')

print("Hello\tWorkd")
print('iteheima\tbest')

"""

"""
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f'{j}*{i}={j*i}\t',end = '')
        j += 1
    i += 1
    print()

"""
"""
name = "itheima"
# for 变量 in 被处理的数据
for x in  name:
    print(x)
"""
"""
name = "itheima is a brand of itcast"

count = 0

for x in name:
    if x == "a":
        count += 1

print(f'被统计的字符串中有:{count}个a')
"""

"""
for x in range(10):
    print(x)

for x in range(5,10):

    print(x)

for x in range(5,20,2):
    print(x)
"""

"""
num = 100
count = 0

for x in range(1,num+1):
    if x % 2 == 0:
        count += 1

print(f"从1到100的之间的偶数数量是：{count}")

"""
# 坚持表白100天，每天都送10多花

# i = 0
# for i in range(1,101):
#     print(f'今天是向小美表达的第{i}天，加油坚持。')
#     for j in range(1,11):
#         print(f'给小美送的第{j}朵玫瑰花')
#     print('小美，我喜欢你')
# print(f'第{i}天，表白成功')

# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f'{j}*{i}={j*i}\t',end='')
#     print()

money = 10000
for i in range(1,21):
    import random
    score = random.randint(1,10)

    if score < 5:
        print(f'员工{i}绩效分{score},不满足，不发工资，下一位')
        continue
    if money >= 1000:
        money -= 1000
        print(f'员工{i}，满足条件发工资1000,公司账户余额{money}')
    else:
        print(f'余额不足，当前余额：{money}元，不足以发工资，不发了，下个月再来')
        break




