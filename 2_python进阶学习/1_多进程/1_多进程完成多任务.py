"""
target:函数方法名
name：进程名（一般不用设置）
group：进程组（目前只用none）
"""
import multiprocessing
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
    coding_process = multiprocessing. Process (target=coding)
    ##创建子进程
    music_process = multiprocessing. Process (target=music)
    #启动进程
    coding_process.start ()
    music_process. start ()