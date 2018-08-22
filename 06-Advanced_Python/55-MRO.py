class Parent(object):
    def __init__(self, name, *args):
        print("Parent init begins")
        self.name = name
        print("Parent init ends")


class Son1(Parent):
    def __init__(self, name, age, *args):
        print("Son1 init begins")
        self.age = age
        super().__init__(name, *args)
        print("Son1 init ends")


class Son2(Parent):
    def __init__(self, name, gender, *args):
        print("Son2 init begins")
        self.gender = gender
        super().__init__(name, *args)
        print("Son2 init ends")


class GrandSon(Son1, Son2):
    def __init__(self, name, age, gender):
        print("Grandson init begins")
        super().__init__(name, age, gender)
        print("Grandson init ends")


print(GrandSon.mro())
gs = GrandSon("Eric", 9, "男")
print("Name: ", gs.name)
print("Age: ", gs.age)
print("Gender: ", gs.gender)
