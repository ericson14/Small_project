class Parent(object):
    def __init__(self, name):
        print("Parent init begins")
        self.name = name
        print("Parent init ends")


class Son1(Parent):
    def __init__(self, name, age):
        print("Son1 init begins")
        self.age = age
        Parent.__init__(self, name)
        print("Son1 init ends")


class Son2(Parent):
    def __init__(self, name, gender):
        print("Son2 init begins")
        self.gender = gender
        Parent.__init__(self, name)
        print("Son2 init ends")


class GrandSon(Son1, Son2):
    def __init__(self, name, age, gender):
        print("Grandson init begins")
        Son1.__init__(self, name, age)
        Son2.__init__(self, name, gender)
        print("Grandson init ends")


gs = GrandSon("Eric", 11, "男")
print("Name: ", gs.name)
print("Age: ", gs.age)
print("Gender: ", gs.gender)
