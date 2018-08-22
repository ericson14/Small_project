class Province(object):
    """Definition"""
    country = "China"

    def __init__(self, name, code):
        self.name = name
        self.code = code

    def func(self):
        print("Name: ", self.name)

    def __call__(self, *args, **kwargs):
        print("Something happened")

    def __del__(self):
        print("Delete")

    def __str__(self):
        return "没毛病老铁"


obj1 = Province("广东", 440000)
print(obj1.__dict__)
print(Province.__doc__)
print(Province.__dict__)
print(obj1.__module__)
print(obj1.__class__)
obj1()
print(obj1)
