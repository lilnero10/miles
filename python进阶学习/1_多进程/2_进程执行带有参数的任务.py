"""
args:以元组的方式给执行任务传参(元组方式传参一定要和参数的顺序保持一致)
kwargs:以字典的方式给执行任务传参(字典方式传参字典中的key一定要和参数名保持一致)
"""

import multiprocessing
import time


def coding(num,name):
    for i in range(num):
        print("coding...")
        print(name)
        time.sleep(0.2)

def music(count):
    for i in range(count):
        print("singing...")
        time.sleep(0.2)

if __name__ == '__main__':
    #创建子进程
    coding_process = multiprocessing. Process (target=coding,args=(10,"nero"))
    ##创建子进程
    music_process = multiprocessing. Process (target=music,kwargs={'count':10})
    #启动进程
    coding_process.start ()
    music_process. start ()