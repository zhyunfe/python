# -*- coding: utf-8 -*-

__author__= 'demoer' # 把作者写进去
# 高级特性

#####################
# 切片               #
#####################
# list
L = ['zhyunfe', 'demor', 'demoer', 'jing']
# 取前n个元素
print(L[0:3])
print(L[:3]) # 如果从0开始，可以忽略
print(L[-2:]) # 取后两个
print(L[-2:-1]) #取倒数第二个 但是是一个list
print(L[-2]) # 取倒数第二个 是一个字符串

N = list(range(100))

# 取前10个数中的偶数
print(N[:10:2])

# 每5个取一个
print(N[::5])

# 复制一个N
M = N[:]
print(M) #[0,1,2,3....]

# tuple 也可以切片
T = (0,1,2,3,4,5,6)
print(T[:3]) # (0,1,2)

 # 字符串也可以切片

S = 'zhyunfe'
print(S[0:2]) # zh


#######################
# 迭代
#######################

##### 字典
d = {'a': 1, 'b': 2}
# 取键
for key in d:
    print(key) # a b
# 取值
for value in d.values():
    print(value) # 1 2 

##### 字符串
S = 'zhyunfe'
for s in S:
    print(s)

# 判断一个对象是否是可迭代对象
from collections import Iterable

print(isinstance('abc', Iterable)) # True
print(isinstance(d, Iterable))     # True
print(isinstance(123, Iterable))   # False

# 实现下标循环
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
'''
0 A
1 B
2 C
'''

for x, y in [(1,1),(2,3),(3,4)]:
    print(x, y)
'''
1 1
2 3
3 4
'''
#######################
# 列表生成
#######################
L1 = list(range(0, 11))
print(L1) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 生成[1 * 1, 2 * 2, 3 * 3 , 4 * 4...]
L2 = [x * x for x in range(1, 11)]
print(L2) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 有判断值的列表生成
L3 = [x * x for x in range(1, 11) if x != 2]
print(L3) #[1, 9, 16, 25, 36, 49, 64, 81, 100]

# 两层循环，生成全排列
L4 = [m + n for m in 'abc' for n in '123']
print(L4) #['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']

# 应用
# 列出当前目录下的所有文件名和目录名
import os
name = [d for d in os.listdir('.')]
print(name) # ['pyecharts', '.DS_Store', 'new_peiqi.png', 'splider', 'wordcloud', 'render.html', '.vscode', 'base']

# for 循环同事使用多个变量
d = {'x':'A','y':'B','z':'C'}
for k, v in d.items():
    print(k, '=', v)
L5 = [k + '=' + v for k, v in d.items()]

# 把list中是所有字符串变成小写
L6 = ['Hello','AbD', 'sdewE']
L7 = [s.lower() for s in L6]
print(L7) #['hello', 'abd', 'sdewe']

# isinstance函数可以判断一个变量是否归属于某一个对象


#########################
# 生成器
#########################

'''
通过列表生成我们可以直接创建一个列表，但是收到内存的限制，列表的容量肯定是有限的，而且创建一个包含100万个列表的元素，不仅
浪费了很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了

如果列表元素可以按照某种算法推算出来，那我们可以在循环过程中不断推算出后续的元素，一边循环一边计算的机制成为 生成器 generator
'''

# 创建一个generator只需要把一个列表生成的[] 改为() 就可以了
L = [x * x for x in range(10)]
print(L) #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
g = (x * x for x in range(10)) # 是一个生成器的对象
print(g) #<generator object <genexpr> at 0x10369a1b0>

# 获取g的内一个元素
g1 = next(g) # 
print(g1) # 0

# 循环获取 因为generator是可迭代的对象
for n in g:
    print(n) # 1，4，9.... 因为0 已经被next了

# 斐波拉契数列，除了第一个和第二个数外，任意一个数都可以由前两个数相加得到
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b # 相当于 t = (b, a + b) a = t[0] b = t[1]
        n = n + 1
    return 'done'
fib(6) # 1 1 2 3 5 8 

# 其实斐波拉契数列就是根据算法逐个算出来的，所以可以考虑使用生成器生成

def gfib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b # 如果一个函数定义中包含了yield关键字，那么这个函数就不是一个普通的函数了，而是一个generator
        a, b = b, a + b
        n = n + 1
    return 'done'

gf = gfib(6)
print(gf) #generator object <genexpr> at 0x10369a1b0>

'''
生成器和函数的执行流程不一样
函数是顺序执行，遇到return语句或者最后一行函数就返回

生成器在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
'''

# example 定义一个generator，依次返回数字1，3，5

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5
o = odd();
print(next(o))
print(next(o))
print(next(o))

# 在使用for循环调用generator时拿不到generator的return语句的返回值
# 如果想拿到返回值，必须捕获StopIteration错误，返回值在StopIteration的value中

gf = gfib(6)
while True:
    try:
        x = next(gf)
        print('g:',x)
    except StopIteration as e:
        print('Generator return value :', e.value)
        break

########################
# 迭代器
########################
# 可以直接作用于for循环的数据类型:
#   集合数据类型list tuple dict set str 
#   生成器：generator
# 这些统称为可 迭代对象 Iterable

# 可以使用isinstance()判断一个对象是否是Interator对象
from collections import Iterator
print(isinstance((x for x in range(10)),Iterator)) #True    generator
print(isinstance([], Iterator))                     #False list
print(isinstance({}, Iterator))                     #False dict
print(isinstance('', Iterator))                     #False str

# list dict 和 str 是可被迭代的，但不是迭代对象,可以使用iter() 函数标称Iterator
a = iter('123')
print(isinstance(a, Iterator))  # True

'''
Python的Iterator对象表示是一个数据流，可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误

可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据
所以Iterator的计算是惰性的，只有在需要返回下一个数据时才会计算

Iterator甚至可以表示一个无限大的数据流，比如全体自然数，而使用list时永远不可能存储全体自然数的
'''


###########################
# 函数式编程
###########################

'''
函数式Python内建支持的一种封装，可以把复杂任务分解成简单的任务，这种分解称之为面向过程的程序设计

函数式编程虽然也可以归结到面向过程的程序设计，但其思想更接近数学计算

在计算机的层次上，CPU执行的是加减乘除的指令代码，以及各种条件判断和指令跳转，所以汇编语言是最贴近计算机的语言
计算则是指数学意义上的计算，越是抽象的计算，离计算机硬件越远

函数式编程的一个特点就是允许把函数本身作为参数传入另一个函数，还允许返回一个函数
'''

# 高阶函数
# 变量可以指向函数

f = abs # 将函数本身赋值给变量，变量可以指向函数
print(f(-1)) # 1

# 函数名也是变量
# abs = 10    # 将变量赋值给函数，函数abs现在就是一个int类型了
# print(abs(-1)) # Tracebck TypeError

# 传入函数
def add(x, y, f):
    return f(x) + f(y)
print(add(5, -6, abs))
# 相当于
print(abs(5) + abs(-6)) # 11

# 把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式


##################
# map/reduce
##################
'''
python 内建了map()和reduce()函数
map()接受两个参数，一个是函数，一个是Iterable
map将传入的函数依次作用于序列的每个元素，并把结果作为新的Iterator返回
'''
def m(x):
    return x * x
l = [1,2,3,4,5,6]
r = map(m, l)
print(list(r)) #[1, 4, 9, 16, 25, 36]   列表里的每个元素都执行一次m函数
s = map(str, l)
print(list(s)) #['1', '2', '3', '4', '5', '6'] 将列表里的每个元素都转化为字符

'''
reduce()
把一个函数作用在一个序列上，这个函数必须接受两个参数，reduce把结果继续和序列的一个元素做累积计算
'''
from functools import reduce

# 函数接受两个参数
def plus(x, y):
    return x + y

red = reduce(plus, [1,2,3,4])
# 相当于 red = puls(plus(plus(1, 2), 3),4) = 1 + 2 + 3 + 4 = 10

#example 把序列[1, 3, 5, 7, 9]变成整数13579
def fn(x, y):
    return x * 10 + y
print(reduce(fn, [1, 3, 5, 7, 9])) 
'''
step1 = fn(1 * 10 + 3) = 13
step2 = fn(step1, 5) = 13 * 10 + 5 = 135
step3 = fn(step2, 7) = 135 * 10 + 7 = 1357
step4 = fn(step4, 9) = 1357 * 10 + 9 = 13579 
'''

# 把字符串'13579' 转换为int
def char2num(s):
    digits = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
    return digits[s]

print(reduce(fn, map(char2num, '13579'))) # 13579

#####################
# filter()
#####################
'''
python 内建的fiter()函数用于过滤序列，filter也接受一个函数和一个序列
fliter把传入的函数依次作用于每个元素，然后根据返回值是True还是False决
定保留还是丢弃该元素
'''

# 判断是不是奇数
def is_odd(n):
    return n % 2 == 1
f = list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10]))
print(f) # 1 5 9

# 把序列中的空字符串删除掉
def not_empty(s):
    return s and s.strip()
n = list(filter(not_empty, ['A', '', 'B', 'None', 'C']))
print(n) # ['A', 'B', 'C']

# filter函数返回的是一个Iterator，是一个惰性序列，所以要强迫filter完成
# 计算结果，需要使用list()函数获得所有结果并返回list

# example 用filter求素数
'''
计算素数是一个埃氏筛法
首先，列出2开始的所有自然数，构造一个序列
取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉
取新序列的第一个数3， 它一定是素数，然后用3把序列的3的倍数筛选掉
...
'''

# 先构造一个从3开始的奇数序列
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

# 定义一个筛选函数
def _not_divisible(n):
    return lambda x: x % n > 0

# 定以一个生成器，不断返回下一个素数
def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

for n in primes():
    if n < 1000:
        print(n)
    else:
        break


#########################
# sorted 排序算法
##########################
l1 = [36, 5, 2, 343, 1]
print(sorted(l1)) # [1, 2, 5, 36, 243]

# 可以接收一个key函数来实现自定义的排序，例如绝对值的大小排序
print(sorted(l1, key=abs)) # 

# 字符串排序 按照ascii
s1 = ['bob', 'about', 'cat']
print(sorted(s1)) # ['about', 'bob', 'cat']

# 倒序排序
print(sorted(s1, key = str.lower, reverse = True))


##############################################
# 返回函数
##############################################

'''
函数作为返回值
'''

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1, 3, 5, 7, 9)
print(f) #<function lazy.sum.<locals>.sum at >
print(f()) # 25

# 在这个例子中我们在lazy_sum中定义了sum，并且内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，相关
# 参数和变量都保存在返回的函数中，这种称为闭包的程序结构拥有极大的威力

# 当我们调用lazy_sum() 时，每次调用都会返回一个新的函数，即使传入相同的参数

###############
# 闭包
###############


###############
# 匿名函数
###############

#我们在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更加方便
l = list(map(lambda x: x * x ,[1, 2, 3, 4, 5, 6, 7])) # 除了定义一个f(x)的函数外，还可以直接传入匿名函数
print(l)# [1, 4, 9, 16, 25, 36, 49]
# 匿名函数lambda x: x * x 实际上就是：
def f1(x):
    return x * x

# 关键字lambda表示匿名函数，冒号前面的x表示函数参数
# 匿名函数有个限制，就是只能有一个表达式，不用些return， 返回值就是该表达式的结果，用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突
# 匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数
f = lambda x: x * x
print(f(5))

# 同样，也可以把匿名函数作为返回值返回，比如：
def build(x, y):
    return lambda: x * x + y * y


################
# 装饰器
################
def now():
    print('2018-01-01')
f = now
print(f())

# 函数对象有一个__name__属性，可以拿到函数的名字
print(now.__name__) # now
print(f.__name__) # now

# 现在，我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now函数的定义，这种在代码运营期间动态增加功能的方式，称为装饰器
# 装饰器可以接受一个函数作为参数，并返回一个函数
def log(func):
    # 新定义一个wrapper函数，可以接收任意参数
    def wrapper(*args, **kw):
        # 先执行装饰器要执行的动作
        print('call %s():' % func.__name__)
        # 再执行被装饰函数要执行的动作
        return func(*args, **kw)
    return wrapper

@log
def now1():
    print('2018-01-01')

print(now1) # call now(): 2018-01-01

# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂，比如要自定义log的文本
def log1(text):
    # 先执行log1 函数，返回decorator函数
    def decorator(func):
        # 执行decorator函数，返回wrapper函数
        def wrapper(*args, **kw):
            # 执行wrapper函数，参数是now函数
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log1('execute')
def now2():
    print('2018-01-01')

print(now()) # execute now(): 2018-01-01
print(now.__name__) # wrapper 经过decorator函数装饰之后的函数，他们的__name__已从原来的now变成了wrapper
# 因为返回的那个wrapper函数名字就是wrapper，所以需要把原始的__name__属性复制到wrapper()函数中
# 不需要编写wrapper.__name__ = func.__name__ 这样的代码
# Python内置的functools.wraps就是干这个事情的

import functools
def log_dec(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper



####################
# 偏函数
####################
'''
Python的functools模块提供了很多有用的功能，其中一个就是偏函数 Partial function
int 函数可以吧字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换
'''
print(int('12345')) # 12345
# int函数还提供额外的base参数，默认值为10，如果传入base参数，就可以做N进制的转换
print(int('12345', base=8)) # 5349
# 假设需要大量转换二进制数据，每次都传入int(x, base=2)非常麻烦，我们想到定义一个int2函数
def int2(x, base=2):
    return int(x, base)
# functools.partial 就是帮助我们创建一个偏函数的，不需要我们自己定义int2(),可以直接使用下面的代码创建一个新的函数int2:

int2 = functools.partial(int, base=2)
print(int2('1000000')) # 64

# 简单的总结，functools.partial的作用就是，把一个函数的某些参数给固定住，返回一个新的函数，调用这个新的函数会更简单



######################
# 模块
######################
'''
在Python中，一个.py文件就称为一个模块
使用模块大大提高了代码的可维护性
使用模块可以避免函数名和变量名冲突
为了避免模块名冲入，Python引入了按目录来组织模块的方法，称为包 (Package))

一个abc.py就是一个abc模块，假设这个模块与其他模块冲突了，可以通过包来组织模块
mypackage
|- __init__.py
|- abc.py
引入了包之后，abc.py模块的名称就编程了mypackage.abc

每一个包目录下面都会有一个__init__.py文件，这个文件是必须存在的，否则Python就会把这个目录当做一个普通目录而不是一个包
__init__.py可以是空文件，也可以有代码


创建模块时要注意：
    模块名要遵循Python变量命名规范，不要使用中文、特殊字符
    模块名不要与系统模块名冲突，最好先查看系统是否已存在该模块，检查方法是在Python交互环境执行 import abc ，如成功则说明已存在
'''

# 使用sys模块
import sys
def test():
    args = sys.argv
    if len(args) == 1:
        print('hello world')
    elif len(args) == 2:
        print('Hello, %s' % args[1])
    else:
        print('Too many arguments')

# 当我们在命令行运行hello模块是时，Python解释器把一个特殊变量__name__置为 __main__
# 而如果在其他地方导入该hello模块时，if判断将失败，因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试

if __name__ == '__main__':
    test()

#######################
# 作用域
#######################
'''
正常的函数和变量名是公开的 public
类似__xx__这样的变量是特殊变量，可以被直接引用，但有特殊用途
类似_xxx和__xxx这样的函数或者变量就是非公开的private 不应该被直接引用
'''

# 安装模块 可以直接使用Anaconda