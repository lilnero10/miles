#定义装饰器1
def check1(fn1):
    def inner1():
        print("登录验证1")
        fn1()
    return inner1

#定义装饰器2
def check2(fn2):
    def inner2():
        print("登录验证2")
        fn2()
    return inner2



@check1
@check2
def commont():
    print("发表评论")

commont()