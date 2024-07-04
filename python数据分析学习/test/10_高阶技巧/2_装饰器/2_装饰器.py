"""
装饰器作用创建一个闭包函数，在闭包函数内调用目标函数
不改动目标函数的同时，增加额外的功能
"""

#装饰器的一般写法（闭包写法）
def outer(func):
    def inner():
        print("睡觉")
        func()
        print("起床")
        return inner()

# def sleep():
#     import random
#     import time
#     print("睡觉中")
#     time.sleep(random.randint(1,5))
#
# fn = outer(sleep) #fn调用outer传入sleep
# fn()

#快捷写法
@outer
def sleep():
    import random
    import time
    print("睡觉中")
    time.sleep(random.randint(1,5))

sleep() #sleep方法没被更改，方法增加了