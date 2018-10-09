############################
#  错误处理
############################
'''
try...
execpt:...
finally...
当我们认为某些代码可能会出错时，就可以用try来运行这段代码，如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，
即except语句块，执行外execpt后如果有finally语句块，则执行finally语句块
'''
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2
def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally')

# 记录错误
'''
如果不捕获错误，自然可以将Python解释器来打印出错误堆栈，但程序也被结束了
Python内置的logging模块可以非常容易地记录错误信息
'''
import logging
def main1():
    try:
        bar('0')
    except Exception as e:
        # 程序打印完错误信息后会继续执行，并正常退出，通过配置，logging可以吧错误记录到日志文件里
        logging.exception(e)

# 抛出错误
# 用raise语句抛出一个错误的实例
class FooError(ValueError):
    pass
def foos(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

#########################
# 调试
#########################
# print
# assert   断言 assert n != 0
# logging 不会抛出错误，可以输出到文件 logging.info() 可以输出一段文本 logging.basicConfig(level = logging.INFO)
    # logging 允许执行记录信息的级别，有debug info warning error
# pdb 让程序以单步方式运行，可以随时查看运行状态 python -m pdb error.py
# pdb.set_trace()
'''
import pdb
s = '0'
n = int(s)
pdb.set_trace() # 运行到这里会自动暂停
print(10 / n)
'''



#########################
# 单元测试
#########################