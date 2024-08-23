class Person(object):
    def __init__(self):
        self.age = 0

    # 获取属性，把age方法定义为属性
    @property 
    def age(self):
        return self.age

    # 修改属性
    @age.setter
    def age(self, new_age):
        self.age = new_age

p = Person()
print(p.age)

p.age = 100
print(p.age)