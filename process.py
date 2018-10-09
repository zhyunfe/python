# 未完成
#####################
# 进程和线程
#####################

'''
对于操作系统来说，一个任务就是一个进程process，有些进程不止同时干一件事情比如word，在一个进程内部需要干许多事情，这些子任务称为线程
由于每个进程至少要干一件事情，所以一个进程至少有一个线程

在Python中如何执行多个任务：
    1、启动多个进程，每个进程虽然只有一个线程，但多个进程可以一块执行多个任务（多进程）
    2、启动一个进程，在一个进程内启动多个线程，多个线程可以一块执行多个任务 （多线程）
    3、启动多个进程，每个进程启动多个线程   （多进程 + 多线程）

同时执行多个任务通常各个任务之间并不是没有关联的，而是需要相互通信和协调，有时任务1必须暂停等待任务2完成之后才能继续执行

线程是最小的执行单元，而进程由至少一个线程组成，如何调度进程和线程完全由操作系统决定，程序自己不能决定什么时候执行，执行多长时间
'''

########
# 多进程
########
'''
Unix/Linux 操作系统提供了一个fork()系统调用，它非常特殊，普通的函数调用，调用一次返回一次，但是fork()调用一次返回两次，因为操作
系统自动把当前进程(父进程)复制了一份(子进程) 然后分别在父进程和子进程内返回

子进程永远返回0，父进程返回子进程的ID，这样的做的理由是一个父进程可以fork出很多子进程，所以父进程要记下每个子进程的ID，而子进程只需要
调用getppid()就可以那都父进程的ID

Python的os模块封装了常见的系统调用，包括fork，可以在Python程序中轻松创建子进程
'''

import os
print('Porcess (%s) start ...' % os.getpid())
pid = os.fork()
if pid == 0:
    print('I am a child process (%s) and my parent is %s' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just create a child process (%s)' % (os.getpid(), pid))

# 有了fork调用，一个进程在接到新任务时就可以复制出一个子任务来处理新任务，常见的Apache服务器就是由父进程监听端口，每当有新的http请求时，就fork出子进程来处理新的http请求

# multiprocessing
# multiprocessing 模块时一个跨平台版本的多进程模型，提供了一个Process类来表示一个进程对象
from multiprocessing import Process
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


print('Parent process %s' % os.getpid())
# 创建一个Process实例
p = Process(target=run_proc, args=('test',))
print('Child process will start')
# 用start方法启动
p.start()
# join方法等待子进程结束后再继续往下运行
p.join()
print('Child process end')



# Pool
# 如果要启动大量的子进程，可以使用进程池的方法批量创建子进程
from multiprocessing import Pool
import time, random
def long_time_task(name):
    print('Run task %s (%s)' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds' % (name, (end - start)))


print('Parent process %s' % os.getpid())
# 同时跑4个进程 Pool的默认大小是CPU的核数
p = Pool(4)
for i in range(5):
    p.apply_async(long_time_task, args=(i,))
print('Waitting for all subprocesses done ...')
p.close()
# Pool对象调用join方法会等待所有子进程执行完毕，调用join之前必须先调用close，调用close之后就不能添加新的process了
p.join()
print('All subprocesses done')

# 子进程
# 很多时候子进程并不是自身，而是一个外部进程，我们创建了子进程后还需要控制子进程的输入和输出
# subprocess 模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出
import subprocess
print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)
