import math


def general_term(n):
    """斐波那契数列通项公式"""
    left = (1+math.sqrt(5))/2
    right = (1-math.sqrt(5))/2
    return 1/math.sqrt(5)*(math.pow(left, n)-math.pow(right, n))


def fib_generator(num):
    n1 = 1
    n2 = 1
    index = 0
    while index < num:
        para = yield n1
        if para is None:
            n1, n2 = n2, n1 + n2
            index += 1
        else:
            n1 = general_term(para)
            n2 = general_term(para+1)
            index = para - 1


f = fib_generator(12)
print(f.send(None))
print(int(f.send(3)))
print(int(f.send(5)))
print(int(f.send(11)))
print(int(next(f)))
