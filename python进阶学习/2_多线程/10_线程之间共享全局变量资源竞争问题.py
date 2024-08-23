"""
sum_num1、sum_num2同时进行，sum_num1先加1赋值给g_num，sum_num2也执行加1赋值给g_num，会出现重复赋值
解决方法：互斥锁
"""
import threading

g_num = 0

def sum_num1():
    for i in range(1000000):
        global g_num
        g_num += 1
    print("g_num1=", g_num)

def sum_num2():
    for i in range(1000000):
        global g_num
        g_num += 1
    print("g_num2=", g_num)

if __name__ == "__main__":
    #创建线程
    sum1_thread = threading.Thread(target=sum_num1)
    sum2_thread = threading.Thread(target=sum_num2)

    #启动线程
    sum1_thread.start()
    sum2_thread.start()