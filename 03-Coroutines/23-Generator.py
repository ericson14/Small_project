def fib_gene(n):
    current = 0
    num1, num2 = 0, 1
    while current < n:
        num = num1
        num1, num2 = num2, num1+num2
        current += 1
        yield num
    return current


if __name__ == '__main__':
    F = fib_gene(5)
    print(type(F))
    while True:
        try:
            x = next(F)
            print("Value: {}".format(x))
        except StopIteration as e:
            print("生成器返回值：{}".format(e.value))
            break

# 88半天上课，10天全天上课
# 161天在校，63天自习（放假），只上了54天课
