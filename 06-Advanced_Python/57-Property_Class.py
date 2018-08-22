class Foo(object):
    def get_bar(self):
        print("Getter")
        return "Laowang"

    def set_bar(self, value):
        print("Setter")
        return "Value" + value

    def del_bar(self):
        print("Deleter")
        return "Laowang"

    BAR = property(get_bar, set_bar, del_bar, "Description...")


obj = Foo()
m = obj.BAR
print(m)
n = obj.BAR = "Alex"
print(n)
desc = Foo.BAR.__doc__
print(desc)
del obj.BAR
