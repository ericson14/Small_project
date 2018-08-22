from functools import wraps
from time import ctime


class Descriptor(object):
    def __init__(self, text=None, *args):
        self.text = text
        self.args = args

    def __call__(self, func=None, *args, **kwargs):
        if callable(self.text):
            self.func = self.text
            print("Name:", self.func.__name__)
            # print("1号参数：{}，2号参数：{}，3号参数：{}".format(*args))
            return self.func(func, *args, **kwargs)
        else:
            print(self.text, self.args)
            self.func = func
            return self.func


def make_bold(fn):
    print("加粗")

    @wraps(fn)
    def wrap():
        return "<b>" + fn() + "</b>"
    return wrap


def make_italic(fn):
    print("倾斜")

    @wraps(fn)
    def wrap():
        return "<i>" + fn() + "</i>"
    return wrap


def time_fun(text):
    if not callable(text):
        def time_fun_args(fn):
            @wraps(fn)
            def rap(*args):
                print("{} is called at {}".format(fn.__name__, ctime()))
                print(*args)
                print(text)
                return fn(*args)
            return rap
        return time_fun_args
    else:
        @wraps(text)
        def wrap(*args):
            print("{} is called at {}".format(text.__name__, ctime()))
            print("*******", *args)
            return text(*args)
        return wrap


@time_fun("Itcast")
@make_bold
@make_italic
def tes():
    return "Itheima"


@Descriptor
def main(a, b, c):
    print("88")
    return a+b+c


print(tes())
print(tes.__name__)
print(main(3, 5, 7))
