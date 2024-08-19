""""
互斥锁：对共享数据进行锁定，保证同一时刻只有一个线程去操作
互斥锁是多个线程一起去抢，抢到锁的线程先执行，没有抢到锁的线程进行等待，等锁使用完释放后，其它等待的线程再去抢这个锁
"""
import threading

g_num = 0
def sum_num1():
    # 上锁
    mutex.acquire()
    for i in range(1000000):
        global g_num
        g_num += 1
    #解锁
    mutex.release()
    print("g_num1=", g_num)

def sum_num2():
    # 上锁
    mutex.acquire()
    for i in range(1000000):
        global g_num
        g_num += 1
    #解锁
    mutex.release()
    print("g_num2=", g_num)

if __name__ == "__main__":
    #创建锁
    mutex = threading.Lock()

    #创建线程
    sum1_thread = threading.Thread(target=sum_num1)
    sum2_thread = threading.Thread(target=sum_num2)

    #启动线程
    sum1_thread.start()
    sum2_thread.start()