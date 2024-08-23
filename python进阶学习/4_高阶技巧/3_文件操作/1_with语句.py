"""
with语句：
操作简捷，不用关闭文件
安全操作，如果文件产生异常，依然可以关闭文件
上下文管理器：
一个类只要实现了_enter_()和_exit_()这个两个方法
通过该类创建的对象我们就称之为上下文管理器
Python提供了with语句用于简化资源释放的操作，使用with语句操作
建立在上下文管理器（实现_enter_和_exit_方法）的基础上
"""
# with open(" ","r") as f:
#     file_data = f.read()
class File(object):
    def __init__(self,file_name,file_model):
        self.file_name = file_name
        self.file_model = file_model

    def __enter__(self):
        print("上文")
        self.file = open(self.file_name, self.file_model)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

    with open("test.txt", "w") as f:
        file_data = f.readlines()
        print(file_data)
