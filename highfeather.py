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