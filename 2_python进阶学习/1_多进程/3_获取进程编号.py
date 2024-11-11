"""
进程编号的作用： 当程序中进程的数量越来越多，就无法区分主进程和子进程还有不同的子进程.实际上为了方便管理每个进程
都是有自己的编号的，通过获取进程编号就可以快速区分不同的进程.
def work() :
    #获取当前进程的编号
    print ("work进程编号:", os.getpid())
    #获取父进程的编号
    print ("work进程编号:", os.getppid())
"""
import os
import multiprocessing
import time


def coding(num,name):
    print("coding>>>%d" % os.getpid())
    print("coding父进程>>>%d" % os.getppid()) #获取父进程id
    for i in range(num):
        print("coding...")
        print(name)
        time.sleep(0.2)

def music(count):
    print("singing>>>%d" % os.getpid())
    print("singing父进程>>>%d" % os.getppid()) #获取父进程id
    for i in range(count):
        print("singing...")
        time.sleep(0.2)

if __name__ == '__main__':
    #获取主进程id
    print("主进程>>>%d" % os.getpid())
    #创建子进程
    coding_process = multiprocessing. Process (target=coding,args=(10,"nero"))
    ##创建子进程
    music_process = multiprocessing. Process (target=music,kwargs={'count':10})
    #启动进程
    coding_process.start ()
    music_process. start ()
