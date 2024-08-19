"""
线程是程序执行的最小单位，实际上进程只负责分配资源，而利用这些资源执行程序的是线程，也就说进程是线程的 容器，一个进程中最少有
一个线程来负责执行程序，同时线程自己不拥有系统资源，只需要一点儿在运行中必不可 少的资源，但它可与同属一个进程的其它线程共享进程
所拥有的全部资源.这就像通过一个QQ软件（一个进程）打开两个窗口（两个线程）跟两个人聊天一样，实现多任务的同时也节省了资源
1.多线程是Python程序中实现多任务的一种方式.
2.线程是程序执行的最小单位.
3.同属一个进程的多个线程共享进程所拥有的全部资源.
"""
import threading
import time

def coding():
    for i in range(10):
        print("coding...")
        time.sleep(0.2)

def music():
    for i in range(10):
        print("singing...")
        time.sleep(0.2)

if __name__ == '__main__':
    #创建子进程
    coding_thread = threading.Process (target=coding)
    ##创建子进程
    music_thread = threading.Process (target=music)
    #启动进程
    coding_thread.start ()
    music_thread. start ()