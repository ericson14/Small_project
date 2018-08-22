class FibIterator(object):
    def __init__(self, n):
        self.n = n
        self.current = 0
        self.num1 = 0
        self.num2 = 1

    def __next__(self):
        if self.current < self.n:
            item = self.num1
            self.num1, self.num2 = self.num2, self.num1+self.num2
            self.current += 1
            return item
        else:
            raise StopIteration

    def __iter__(self):
        return self


if __name__ == '__main__':
    fib = FibIterator(20)
    for num in fib:
        print(num, end=" ")
    print("\n", list(FibIterator(10)))
