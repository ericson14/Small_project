# 可迭代对象->iter->返回迭代器->iter->返回自身->next->返回下一个迭代
class MyList(object):
    def __init__(self):
        self.items = []

    def add(self, val):
        self.items.append(val)

    def __iter__(self):
        myiterator = MyIterator(self)
        return myiterator


class MyIterator(object):
    def __init__(self, mylis):
        self.mylis = mylis
        self.current = 0

    def __next__(self):
        if self.current < len(self.mylis.items):
            item = self.mylis.items[self.current]
            self.current += 1
            return item
        else:
            raise StopIteration

    def __iter__(self):
        return self


if __name__ == '__main__':
    mylist = MyList()
    mylist.add(1)
    mylist.add(2)
    mylist.add(3)
    mylist.add(4)
    mylist.add(5)
    for ite in mylist:
        print(ite)
