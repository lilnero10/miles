"""
装饰器的作用：
在不改变原有函数的源代码的情况下，给函数增加新的功能
装饰器的功能特点：
①不修改已有函数的源代码
②给已有函数增加额外的功能
"""
import random
import time

#装饰器的一般写法（闭包写法）
def outer(func):
    def inner():
        print("睡觉")
        func() #相当于调用外部定义的sleep()函数
        print("起床")
    return inner()

#需要被装饰的函数sleep()
def sleep():
    print("睡觉中")
    time.sleep(random.randint(1,5))
sleep = outer(sleep)
sleep()

#快捷写法
@outer
def sleep():
    print("睡觉中")
    time.sleep(random.randint(1,5))
sleep()