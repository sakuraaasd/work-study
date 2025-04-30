"""
本代码演示了：
-各类字面量的写法
-通过print语句输出各类字面量
"""

print("键盘敲烂")
print("月薪过万")
print("学It就来黑马程序员")
print("Hello World")
print("hhhh")
print("hhhh")

# 写一个整数字面量
666
# 写一个浮点数字面量
13.14
# 写一个字符串字面量
"黑马程序员"

# 通过print语句输出各类字面量
print(666)
print(13.14)
print("黑马程序员")

# 空一行写注释 遵循官网规范

# 通过一个变量，记录钱包的余额
money=50
# 输出print语句，输出变量记录的内容
print("钱包还有：",money)

# 买了一个冰激凌，话费了10元，用英字,将内容隔开
money=money-10
print("买了冰淇淋花费10元，还剩余：",money,"元")

# 假设，每隔一小时输出一下钱包的余额
print("现在是下午1点，钱包余额剩余：",money)
print("现在是下午2点，钱包余额剩余：",money)
print("现在是下午3点，钱包余额剩余：",money)
print("现在是下午4点，钱包余额剩余：",money)

# 变量名=变量值（特征：变量的值可以发生改变的）
print(type("heima"))
print(type(666))
print(type(13.14))

# 方式1:使用print直接输出类型信息
print(type("黑马程序员"))
print(type(666))
print(type(13.14))

# 方式2:使用变量储存type（）语句的结果
string_type=type("黑马程序员")
int_type=type(666)
float_type=type(13.14)
print(string_type)
print(int_type)
print(float_type)

# 方式3:使用type（）语句，查看变量中存储的数据类型信息
name="黑马程序员"
name_type=type(name)
print(name_type)

# 将数字类型转换成字符串
num_str=str(11)
print(type(num_str))
float_str=str(13.14)
print(type(float_str))

# 将字符串转换成数字
num=int("11")
print(type(num))

num2=float("11.34")
print(type(num2),num2)

# 整数转浮点数
num3=float(11)
print(type(num3),num3)

# 浮点数转整数
num4=int(14.94)
print(type(num4),num4)

# 规则1:内容限定，限定只能使用：中文，英文，数字，下划线，注意：不能以数字开头
# name_! = "张三" 错误的代码示范
name_ = "张三"
_name = "张三"

# 规则2:大小写敏感
Itheima = "黑马程序员"
itheima = 666
print(Itheima)
print(itheima)

# 规则3:不可以使用关键字
# class = 1
# def = 1
Class = 1

# 标识符：变量的名，类名，方法名！！！！
# 内容限定（只能使用：中文，英文，数字，下划线）；大小写铭感；不可以使用关键字
# 变量的命名规范：1：明了，看到名字就知道什么意思。2：多个单词组合的时候要用下划线分割。3:英文字母全部小写

"""
演示python中的各类运算符号
"""
# 算数（数学）运算符
print("1 + 1 = ",1 + 1)
print("2 - 1 = ",2 - 1)
print("3 * 3 = ",1 * 1)
print("4 / 2 = ",4 / 2)
print("11 // 2 = ",11 // 2)
print("9 % 2 = ",9 % 2)

# 赋值运算符
num = 1 + 2 * 3
# 复合赋值运算符
#  +=
num = 1
num += 1
print("num += 1:",num)
num -= 1
print("num -= 1:",num)
num *= 4
print("num *= 4:",num)
num /= 2
print("num /= 2:",num)
num = 3
num %= 2
print("num %= 2:",num)
num **= 2
print("num **=2:",num)
num = 9
num //= 2
print("num //= 9:",num)

# 字符串的定义形式：1，单引号；2，双引号；3，三引号（支持换行操作）
# 单引号定义法：
name = '黑马程序员'
print(type(name))
# 双引号定义法
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
# 在字符串内包含单引号
name = "'黑马程序员'"
# 使用转译字符\解除引号的效用
name = "\"黑马程序员\""
print(name)
name = '\'黑马程序员\''
print(name)

# 字符串字面量之间的拼接
print('学IT来黑马'+'月薪过万')
# 字符串字面量和字符串变量的拼接
name = "黑马程序员"
address = "建材城东路9号院"
print('我是：'+name+'，我的地址是：'+address)

# 通过占位的方式，完成拼接
name = '黑马程序员'
message = '学IT来：%s'%name
print(message)
# 通过站位的形式，完成数字和字符串的拼接
class_num = 57
avg_salary = 16781
message = "Python大数据学课，北京%s期，毕业平均工资：%s" %(class_num,avg_salary)
print(message)

name = '传智博客'
setup_year = 2006
stock_price = 19.99
message = '%s,成立于:%d,我今天的股价是%f'%(name,setup_year,stock_price)
print(message)

num1 = 11
num2 = 11.345
print("数字11宽度限制5，结果是：%5d" % num1)
print("数字11宽度限制1，结果是：%1d" % num1)
print("数字11宽度限制7，小数精度是2，结果是：%7.2f "% num2)
print('数字11小数精度是2，结果是%.2f'%num2)

# f"{占位}"
name = "传智博客"
set_up_year = 2006
stock_price = 19.99
print(f'我是：{name},我成立于：{set_up_year},今天的股价是{stock_price}')

print("1*1的结果是：%d"%(1*1))
print(f'1*2的结果是：{1*2}')
print('字符串在python中的类型名称是：%s'%type("字符串"))

name = "传智博客"
stock_price = 19.99
stock_code = "003032"
stock_price_daily_growth_factor = 1.2
growth_days = 7
finally_storck_prick = stock_price*stock_price_daily_growth_factor**growth_days
print(f"公司：{name}，股票代码：{stock_code},当前股价：{stock_price}")
print("每日增长系数：%.1f，经过%d天的增长后，股价达到了：%.2f"%(stock_price_daily_growth_factor,growth_days,finally_storck_prick))


# name = input("请告诉我你是谁？")
# print('我知道了，你是：%s' % name)

# 输入数字类型
# num = input('请告诉我你的银行卡密码：')
# num = int(num)
# print('你的银行卡密码的类型是：',type(num))

黑马程序员 = input("user_name")
SSSSSVIP = input("user_type")
print(黑马程序员,"您是尊贵的：",SSSSSVIP,"用户，欢迎您的光临")

# 单引号定义法
name = '黑马程序员'
print(type(name))
