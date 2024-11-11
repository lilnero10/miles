class Phone:

    __current_voltage = None #私有成员

    #私有方法
    def __keep_single_core(self):
        print("让CPU单核运行")


phone = Phone()
