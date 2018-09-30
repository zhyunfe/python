#coding=utf-8
a = -12
# 取正
aa = abs(-12)
print(aa) # 12

# 取最大值
b = max(1, 2, 3, 4)
print(b) # 4

#数据类型转换
intN = int('123')
print(intN) # 123

intF = int(123.34)
print(intF) # 123

floatN = float('123.4') 
print(floatN) # 123.4

strN = str(123)
print(strN) #'123'

boolN = bool(1)
print(boolN) # True
boolNF = bool('')
print(boolNF) # False

# 函数变量
a = abs # 变量a指向abs函数
print(a(-1)) # 1

# 定义函数
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-10)) # 10

# 如果将my_abs放在了abstest.py文件，可以使用from abstest import my_abs
from demor import my_max
print(my_max([1,2,3,4,5]))

# 空函数
def nop():
    pass # pass语句什么都不做，可以当做一个占位符

# 检查参数类型
def my_check(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    return x

# 返回多个值
import math
def move(x, y, step, angle = 0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
x, y = move(100, 100, 60, math.pi / 6)
print(x, y) #151.96152422706632 70.0
r =move(100, 100, 60, math.pi / 6)
print(r) # (151.96152422706632, 70.0)

# 返回值是一个tuple，在语法上一个tuple可以省略口号

# 函数的参数

# 可变参数
# 在python中，可以定义可变参数，传入的参数个数是可变的可以是1、2到任意个，也可以是0个
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc([1, 2, 3, 4]))

# 使用*numbers 就可以简化
def calc_c(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc_c(1, 2, 3)) # 3个参数
print(calc_c())        # 0个参数
print(calc_c(1))       # 1个参数
# 还可以这样，把list中的所有元素作为可变参数传进去
num = [1, 2, 3]
print(calc_c(*num))


# 关键字参数
# 关键字参数允许你传入0个或者任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
# 可以扩展函数功能
def person(name, age, **k):
    print('name:', name, 'age:', age, 'other', k)

print(person('zhyunfe', 12)) # name:zhyunfe age: 12 other: {}

print(person('zhyunfe', 12, city='guangzhou')) # name:zhyunfe age:12 other: {'city': 'guangzhou'}

extra = {'city': 'guangzhou', 'job:': 'engineer'}
person('zhyunfe', 12, **extra)


# 命名关键字参数
# 对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数，至于到底传入了哪些参数，需要在函数内部通过k检查
def person2(name, age, **k):
    if 'city' in k:
        pass
    if 'job' in k:
        pass
    print('name:', name, 'age:', age, 'other', k)
# 但是还是可以传入任意别的参数，如果要限制关键字参数的名字，就要用命名关键字参数，例如只接受city和job作为关键字
def person3(name, age, *, city, job):
    print('name:', name, 'age:', age, 'city:', city, 'job', job)

# 如果函数定义了一个可变参数，后面的命名关键字参数就不再需要一个特殊的分割符号了

def person4(name, age, *args, city, job):
    print(name, age, args, city, job)
# 命名关键字参数必须要传入参数名



# 递归函数
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1) # 函数在返回return时参数计算
# 使用递归函数需要防止栈溢出
# 在计算机中，函数调用时通过栈这种数据结构实现的，每当进入一个函数调用，就会增加一层栈帧，每当函数返回就会减少一层栈帧
# 由于栈的大小不是无限的，所以当递归调用次数过多，就会导致栈溢出

# 解决栈溢出就要使用 尾递归 优化

def fact1(n):
    return fact_iter(n, 1)
# 尾递归函数
def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product) # 仅仅返回函数本身，函数本身不会参与到运算
# 尾递归是指在函数返回的时候，调用自身本身，并且，return 语句不能包含表达式，这样编译器或者解释器就可以把尾递归做优化，使得递归本身无论调用多少次，都只用一个栈帧

# 但是
# 大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，所以还是会溢出








