from datetime import datetime
import sys


def main():
    print("当前时间：", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    now = datetime.now()
    minu = now.minute
    h = now.hour
    y = now.year
    m = now.month
    d = now.day
    s = 0
    if 8 <= minu <= 22:
        minu = 15
    elif 23 <= minu <= 37:
        minu = 30
    elif 38 <= minu <= 53:
        minu = 45
    elif 54 <= minu <= 59:
        minu = 0
        if h < 23:
            h += 1
        else:
            h = 0
            d += 1
    else:
        minu = 0
    print("{}-{:0>2d}-{:0>2d} {:0>2d}:{:0>2d}:{:0>2d}".format(y, m, d, h, minu, s))

    for path in sys.path:
        print(path)


if __name__ == '__main__':
    main()
