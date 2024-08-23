#闭包不仅可以保存外部函数的变量还可以提高代码的复用性
#外部函数
def config_name(name):
    def say_info(info):
        print(name+""+info)
    return say_info

tom = config_name ("tom")
tom("你好")
tom("你在吗")
jerry = config_name("jerry")
jerry("你好")
jerry("我在呢")