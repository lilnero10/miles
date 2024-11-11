class Person(object):
    def __init__(self):
        self.age = 0

    def get_age(self):
        return self.age


    def set_age(self, new_age):
        if new_age > 150:
            print("error")
        else:
            self.age = new_age

    age = property(get_age, set_age)

p = Person()
p.age = 100
print(p.age)