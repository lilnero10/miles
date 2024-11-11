class Phone:
    ID = None
    Producer = "APPLE"

    def call_by_5g(self):
        print('使用5g通话')

#定义子类，复写父类
class Myphone(Phone):
    Producer = "Pineapple"

    #方法1
    #print(f"父类的厂商是：{Phone.Producer}")
    #Phone.call_by_5g(self)
    #方法2
    print(f"父类的厂商是：{super().Producer}")
    super().call_by_5g()
    print("关闭CPU单核模式")

