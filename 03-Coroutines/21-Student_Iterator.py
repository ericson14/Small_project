from collections import Iterator
from collections import Iterable


class StudentList(object):
    def __init__(self):
        self.items = []

    def append_std(self, item):
        self.items.append(item)

    def __iter__(self):
        itor = StudentIterator(self.items)
        print("你发现了这里！", isinstance(itor, Iterator))
        return itor


class StudentIterator(object):
    def __init__(self, items):
        self.items = items
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.items):
            self.index += 1
            return self.items[self.index-1]
        else:
            raise StopIteration


s1 = StudentList()
print("s1可迭代吗？", isinstance(s1, Iterable))
s1.append_std("张三")
s1.append_std("李四")
s1.append_std("王五")
s1.append_std("赵六")

# for s in s1:
#     print(s)

tor = iter(s1)
print(tor)

# print(next(tor))

while True:
    try:
        print(next(tor))
    except StopIteration:
        break
