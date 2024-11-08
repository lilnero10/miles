#定义一个类，实现__call__方法
class Check():
    def __call__(self, *args, **kwargs):
        print("这是call方法")

c = Check()
c()



#定义类装饰器
class Check(object):
    def __init__(self, fu):
        self.__fu = fu
    def __call__(self, *args, **kwargs):
        print("登录")
        self.__fu()
@Check # comment = Check(comment)
def comment():
    print("发表评论")




