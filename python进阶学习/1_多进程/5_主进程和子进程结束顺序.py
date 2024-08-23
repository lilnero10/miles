"""
主进程会等待所有的子进程执行结束再结束
"""

import multiprocessing
import time


def work() :
    for i in range (10):
        print("工作中...")
        time.sleep (0.2 )

if __name__ == "__main__":
    #创建子进程
    work_process = multiprocessing. Process (target=work)
    
    # #1.设置守护主进程
    # work_process.daemon = True
    # #2.让子进程直接销毁，表示终止执行，主进程退出之前，把所有的子进程直接销毁就可以了
    # work_process.terminate()

    work_process.start()
    #让主进程等待1秒钟
    time.sleep(1)
    print("主进程执行完成了")