import os
from os import path

# io编程


# 文件读写
'''
读取文件是最常见的IO操作，Python内置了读写文件的函数，用法和C是兼容的
'''
d = path.dirname(__file__) if '__file__' in locals() else os.getcwd()
f = open(path.join(d, 'test.txt'), 'r') # 以只读方式读取一个文件
print(f.read()) # 
f.close() # 文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的

# 由于文件读写时都有可能产生IOError，一旦出错后f.close()就不会调用，所以为了保证无论是否错误都正确关闭文件，我们可以使用try...finally实现
try:
    f = open(path.join(d, 'test.txt'), 'r')
    print(f.read())
finally:
    if f:
        f.close()

# 但是每次这样写比较繁琐，所以Python引入了with语句帮助我们自动调用close()方法
with open(path.join(d, 'test.txt'), 'r') as f:
    print(f.read())

# 调用read() 会一次性读取文件的全部内容，如果有10G，内存就爆了，所以保险起见，可以反复使用read(size)

# 如果文件很小，read()一次性读取最方便，如果不能确定文件大小，反复调用read(size)比较保险，如果是配置文件，调用readlines()最方便
f = open(path.join(d, 'test.txt'), 'r')
for line in f.readlines():
    print(line.strip()) # 把末尾的'\n'删掉

# 二进制文件
f = open(path.join(d, 'test.jpg'), 'rb')
print(f.read())


# 字符编码
# 要读取非UTF-8编码的文本文件，需要给open()传入encoding参数,遇到编码不规范的文件，可以传入errors参数直接忽略
f = open(path.join(d, 'test.txt'), 'r', encoding='gbk', errors='ignore')


# 写文件 a 是追加
with open(path.join(d, 'text.txt'), 'w') as f:
    f.write('zhyunfe')


# 操作文件和目录
print(os.name) # posix 操作系统类型
print(os.uname()) # 详细的系统信息
print(os.environ) # 操作系统定义的环境变量
# 获取某一个环境变量的值
os.environ.get('PATH')
# 查看当前目录的绝对路径
print(os.path.abspath('.')) #/usr/local/study/python/base
# 在某个目录下创建一个新的目录
os.mkdir(path.join(d, 'testdir'))
# 删除一个目录
os.rmdir(path.join(d, 'testdir'))

# 拆分路径时不要直接去拆字符串，要通过os.path.split() 函数
# 拆分为两部分，后一部分为最后级别的目录或者文件名
print(os.path.split('/usr/local/var/www/test.txt'))

# 获取文件的扩展名
print(os.path.splitext('/usr/local/var/www/test.txt')) # ('/usr/local/var/www/test', '.txt')

# 文件重命名
# os.rename(path.join(d, 'test.txt'), path.join(d, 'rename.txt'))
# 删掉文件
# os.remove(path.join(d, 'rename.txt'))

# 利用Python过滤文件
# 列出当前目录下的所有目录
l = [x for x in os.listdir('.') if os.path.isdir(x)]
print(l)
# 列出当前目录下所有.py文件
l1 = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
print(l1)

############################
# 序列化
############################
# 我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中交pickling，序列化后就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上
# 把变量内容从序列化的对象重新读取到内存里称之为反序列化，即unpickling

import pickle
dic = dict(name='non', age = 20, score = 88)
print(pickle.dumps(d)) #b'\x80\x03}q\x00(X\x04\x00\x00\x00nameq\x01X\x03\x00\x00\x00nonq\x02X\x03\x00\x00\x00ageq\x03K\x14X\x05\x00\x00\x00scoreq\x04KXu.'

# pickle.dumps() 把任意对象序列化成一个bytes，然后就可以把这个bytes写入文件或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object:
with open(path.join(d, 'dump.txt'), 'wb') as f:
    pickle.dump(dic, f)

with open(path.join(d, 'dump.txt'), 'rb') as f:
    dic = pickle.load(f)
    print(dic) # {'name': 'non', 'age': 20, 'score': 88}



###############################
# JSON
###############################

'''
如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式
最好的方法是序列化为JSON， JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输
JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便
'''

import json
d = dict(name = 'non', age = 28, score = 88)
# json序列化
json_d = json.dumps(d)
print(json_d) #{"name": "non", "age": 28, "score": 88}
# json反序列化
print(json.loads(json_d))

# 将一个实例类序列化为json
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
s = Student('Bob', 20, 99)     
# 通常class实例都有一个__dict__属性，用来存储实例变量 定义了__slots__的没有
print(json.dumps(s, default=lambda obj: obj.__dict__))# {"name": "Bob", "age": 20, "score": 99}

# 对象实例反序列化
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

json_str = '{"name": "Bob", "age": 20, "score": 99}';
print(json.loads(json_str, object_hook=dict2student)) #<__main__.Student object at 0x10e7eebe0>

