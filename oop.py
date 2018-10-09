'''
class 类名(继承类，默认写object)
'''
class Student(object):
    # 通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑定上去
    # __init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部
    # 就可以把各种属性绑定到self
    # 有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数
    # 但self不需要传，Python解释器自己会把实例变量传进去
    def __init__(self, name, score, sex):
        self.name = name
        self.score = score
        # private
        # 在Python中，变量名类似__xx__的，是特殊变量，特殊变量是可以直接访问的，不是private变量
        # 所以不能用__name__ __sex__这样的变量名
        # 私有化的变量不可以使用__name访问，但仍然可以通过_Student__name访问
        self.__sex = sex

    def print_score(self):
        print('%s %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return  'B'
        else:
            return 'C'
    def get_sex(self):
        return self.__sex
    
    def __len__(self):
        return 100
    
    # 访问限制
    # 如果让内部属性不被外部访问，就可以把属性的名称前面加上两个下划线__
    # 在Python中实例的变量名如果以__开头，就编程了一个私有变量，只有内部可以访问

bart = Student('bar', 59, '男')
lisa = Student('lisa', 90, '女')
bart.print_score()
lisa.print_score()


class Animal(object):
    def run(self):
        print('Animal is running...')

# 继承Animal类
class Dog(Animal):
    pass

class Cat(Animal):
    def run(self):
        print('Cat is running')

dog = Dog()
dog.run()

cat = Cat()
cat.run()

# 多态

def run_twice(Animal):
    Animal.run()

run_twice(Animal()) # Animal is running
run_twice(Cat()) # Cat is running


#获取对象的信息
# 获取类型
type(123) # <class 'int'>

# 获取对象的所有属性和方法
dir('ABC')

dir('Animal')

len('ABC') # 相当于'ABC'.__len__
# 如果我们自己写的类想调用len(myObj)的话，就自己写一个__len__方法

print(getattr(bart, 'name')) # 获取属性
print(setattr(bart, 'name','qiqi')) # 设置属性
print(hasattr(bart, 'name')) # 判断是否有属性

################################
# 面向对象高级编程
################################
# 1、使用__slots__
# 限制某一个class实例能添加的属性
class Student2(object):
    __slots__ = ('name', 'age', 'score') # 用tuple定义允许绑定的属性名称，仅仅对当前类实例起作用，对继承的子类是不起作用的


# 2、使用property
# 在绑定属性时，如果我们直接把属性暴露出去，就没有办法检查参数，导致可以任意修改属性
s = Student2()
s.score = 9999
print(s.score)
# 为了限制score的范围，需要一个set_score 和一个get_score来设定和获取成绩
class Student3(object):
    def get_score(self):
        return self._score
    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be iteger!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 - 100!')
        self._score = value

# 操作时，我们使用get_score 和 set_score 
xiaoming = Student3()
xiaoming.set_score(30)
print(xiaoming.get_score)

# 这有一个更为简单的方法，使用@property 将一个方法变成属性
class Student4(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be iteger!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 - 100!')
        self._score = value
xiaohong = Student4()
xiaohong.score = 99 # 这里调用了score.setter
print(xiaohong.score)


##################################
# 多重继承
##################################

class Mammal(Animal):
    pass
class Bird(Animal):
    pass
class Runnable(object):
    pass
class Flyable(object):
    pass

class Dog2(Mammal, Runnable):
    # 继承了Mammal和Runnable，拥有这两个类的所有属性和方法
    pass

#################################
# 定制类
#################################
'''
    __slots__   限制类的属性 __slots__ = ('name', 'age', 'height')
    __len__     能让class作用于len()函数
    __str__     打印一个类,返回字符串
    __repr__    返回程序开发者看到的字符串
    __iter__    一个类想用于for...in循环
    __getitem__ 让一个类像list那样按照小标取出元素
    __getattr__ 动态返回一个属性
    __call__    直接在实例本身上调用
'''

class DiyStudent(object):
    def __init__(self, name):
        self.name = name
    __slots__ = ('age', 'height', 'score')

    def __str__(self):
        return 'Student Object (name, %s)' % self.name

    __repr__ = __str__

    # 如果访问了一个不存在的属性，会在这个函数里查找
    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        raise AttributeError('Student object has no attribute \'%s\'' % attr)

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1
    
    # 让Fib可以作用于for循环
    def __iter__(self):
        return self
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a
    # 让Fib实例可以能像list一样通过下标取出元素
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        # 允许Fib进行切片
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

for n in Fib(): # 可以作用于for循环
    print(n)

f = Fib()
print(f[0])
print(f[1])   # 通过下表获取元素
print(f[0:5]) # 切片









###############################
# 使用枚举类
###############################
from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'))
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value) # value属性是自动付给成员的int常量，默认从1开始计数

'''
    Jan => Month.Jan , 1
    Feb => Month.Feb , 2
    Mar => Month.Mar , 3
    Apr => Month.Apr , 4
    May => Month.May , 5
    Jun => Month.Jun , 6
'''