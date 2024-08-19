"""
一直等待对方释放锁的情景就是死锁,会造成应用程序的停止响应，不能再处理其它任务了
"""
import threading

g_num = 0
def sum_num1():
    # 上锁
    print("sum_num1...")
    mutex.acquire()
    for i in range(1000000):
        global g_num
        g_num += 1
    print("g_num1=", g_num)

def sum_num2():
    # 上锁
    print("sum_num2...")
    mutex.acquire()
    for i in range(1000000):
        global g_num
        g_num += 1
    print("g_num2=", g_num)

if __name__ == "__main__":
    #创建锁
    mutex = threading.Lock()

    #创建线程
    sum1_thread = threading.Thread(target=sum_num1)
    sum2_thread = threading.Thread(target=sum_num2)