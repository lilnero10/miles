"""
•使用工厂类的get_person（）方法去创建具体的类对象
优点：
•大批量创建对象的时候有统一的入口，易于代码维护
•当发生修改，仅修改工厂类的创建方法即可
•符合现实世界的模式，即由工厂来制作产品（对象）
"""
class Person():
    pass

class Student(Person):
    pass

class Worker(Person):
    pass

class Teacher(Person):
    pass

class Factory:
    def get_person(self,p_type):
        if p_type == 'w':
            return Worker()
        elif p_type == 's':
            return Student()
        elif p_type == 't':
            return Teacher()

pf = Factory()
worker = pf.get_person('w')
student = pf.get_person('s')
teacher = pf.get_person('t')