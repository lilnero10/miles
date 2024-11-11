
class Student():
    name = None

#成员方法
    def say_hi(self):
        print(f"大家好，我是{self.name}")


stu = Student()
stu.name = "czy"
stu.say_hi()

