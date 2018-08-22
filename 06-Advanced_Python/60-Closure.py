def line(a, b):
    def para(x):
        return a * x + b
    return para


def count(x=0):
    def incre():
        nonlocal x
        x += 1
        return x
    return incre


def my_avg():
    data = list()

    def add(num):
        data.append(num)
        return sum(data)/len(data)
    return add


if __name__ == '__main__':
    line1 = line(-2, 1)
    line2 = line(3, 6)
    c1 = count(5)
    c2 = count(50)
    avg = my_avg()
    print([line1(x) for x in range(-10, 10)])
    print([line2(x) for x in range(-10, 10)])
    for i in range(20):
        print(c1(), end=" ")
        print(c2(), end=" ")
        print(avg(line2(i)))
