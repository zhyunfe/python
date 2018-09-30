# 打印hello world
print('hello world')
print('arg1', 'arg2', 'arg3')
# 输入
# name = input()
# print(name)

# 数据类型和变量
# 整数、浮点数、字符串
# 布尔值True False 布尔值可以用and or 和 not运算
# age = input()
# if int(age) > 18:
#     print('黄花大闺女')
# else:
#     print('老妇女')
# 空值
# 空值是Python里一个特殊的值，用None表示，None不能理解为0，因为0是有意义的，而None是一个特殊的空值
# 变量
a = 'ABC' # 此时Python解释器干了两个事情 在内存中创建了一个'ABC'的字符串，在内存中创建了一个名为a的变量，并将它指向'ABC'
# 常量，大写的变量名为常量
PI = 3.1415926
# 运算 / 除法，取浮点数 // 地板除，只取整 % 取余数

# 格式化,在Python中，采用格式化的方式和c语言是一致的，用% 实现
age = 'Age: %s . Gender: %s' % (25, True)
print(age) # Age: 25 . Gender: True

# %d 整数 %f 浮点数 %s 字符串 %x 十六进制整数

name = 'Hello, {0}, 成绩提升了{1:.1f}%'.format('小明', 17.25)
print(name)

# 编码 python3 字符串使用Unicode 直接支持多语言每当str和bytes互相转换时，需要制定编码
china = '中国'.encode('gb2312')
print(china)

# 字符串
a = 'abc'

# 替换
A = a.replace('a', 'A')
print(a) # abc
print(A) # Abc

# list
# python 内置的一种数据类型是列表 
# list 是有序的集合，可以随时添加和删除其中的元素
# 查找和插入的时间随着元素的增加而增加
# 占用空间小，浪费内存很少
friend = ['0zhyunfe', '1demor', '2jing', '3kai', '4rui']
print(friend)

# 获取长度
length = len(friend)

# 访问
for i in range(0, length):
    print(friend[i])

# 删除尾部元素
friend.pop()

# 删除制定位置元素
friend.pop(2)

# 替换元素
friend[2] = 't3kkk'

# list 嵌套
classmate = ['sheng', 'cai']

friend.append(classmate)

print(friend) # ['0zhyunfe', '1demor', 't3kkk', ['sheng', 'cai']]

print(friend[3][0]) # sheng

# 排序
a = ['c' ,'b', 'a']
a.sort()
print(a) # a b c

# 元组 tuple tuple 一旦初始化就不能修改
classmates = ('mate2', 'huahua', 'chenxi')

# 定义一个空元组
tuple0 = ()

# 定义一个只有1个元素的元组
tuple1 = (1, ) # 不能写成tuple1 = (1) 因为这样会初始化一个元素为1的元组，要加一个 ','

# 内容可变的元组
list1 = ['tuple1', 'tuple2']
tuple2 = ('1', '2', list1)
tuple2[2][0] = 'tuple3' # ('1','2',['tuple3', 'tuple2'])

# dict
# python 内置了字典，使用键-值存储，
# 具有极快的查找速度，不会随着key的增加而变慢
# 需要占用大量的内存，内存浪费多
# 是用空间换取时间的一种方法
# dict的key必须是不可变对象，因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就
# 完全混乱了，key的计算位置的算法是哈希算法，保证hash的正确性，作为key的对象就不能变
# 字符串、整数都是不可变的，可以作为key，list是可变的，就不能作为key
d = {'zhyunfe':10, 'demor': 20, 'demoer': 30}
print('---------------')
print(d['zhyunfe'])

zhyunfe = d.get('zhyunfe')
zhyunfe1 = d.get('zhyunfe', 'default')
print('===========')
print(zhyunfe)

# set
# set 和 dict类似，也是一组key的集合，但是不存储value，key不能重复
# 要创建一个set，需要提供一个list作为输入集合

s = set([1, 2, 3])
print(s) # 1 2 3
s = set([1, 2, 3, 4, 5, 1, 1])
print(s) # 1 2 3 4 5

# 添加元素
s.add(4) # 1 2 3 4 5 会自动去重

# 删除元素
s.remove(4) # 1 2 3 5

# 取交集
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
s12 = s1 & s2
print(s12) # {2, 3}

# 取并集
s1122 = s1 | s2
print(s1122) # {1, 2, 3, 4}

# 条件判断
age = 28
if age >= 18:
    print('lao niang men')
else :
    print('xiao sao huo')

# elif
if age == 18:
    print('jianhuo')
elif age <  18:
    print('xiaosaohuo')
else:
    print('laoniangmen')




# 循环

# for
num = [1, 2, 3, 4]
for i in num:
    print(i)

# while
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

# break
# continue