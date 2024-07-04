

class Student():
    name = None
    age = None
    tel = None

#构造方法内定义成员变量，使用self关键字，变量定义在构造方法内部，如果要成为成员变量，需要用self表示
    def __init__(self,name,age,tel):
        self.name = name
        self.age = age
        self.tel = tel

    #__str__魔术方法
    def __str__(self):
        return f"Student类对象，name:{self.name},age:{self.age},telephone:{self.tel}"

stu = Student("陈志勇",21, "13829692575")
print(stu)
print(str(stu))