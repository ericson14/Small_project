import re

#
#
# def add(temp):
#     strNum = temp.group()
#     num = int(strNum) + 1
#     return str(num)
#
#
# ret = re.search(r"\d+", "阅读次数为999")
# print(ret.group())
#
# ret = re.findall(r"\d+", "python=999, c=7890, c++=12345")
# print(ret)
#
# ret = re.sub(r"\d+", "998", "python=997")
# print(ret)
#
# ret = re.sub(r"\d+", add, "c++=99")
# print(ret)
#
# ret = re.split(r":|\||\s", "info:xiaozhang|33 shandong")
# print(ret)
#
# test_str = "<p>2、掌握HTTP协议，熟悉MVC、MVVM等概念以及相关WEB开发框架</p>"
# ret = re.sub(r"<[^>]*>", "", test_str)
# print(ret)
#
# url = '<img data-original="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" sr' \
#       'c="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" style="display: inline;">'
# ret = re.search(r"https://.*?\.jpg", url)
# print(ret.group())
#
# labels = ["<html><h1>www.itcast.cn</h1></html>", "<html><h1>www.itcast.cn</h2></html>"]
# for label in labels:
#     ret = re.search(r"<(\w*)><(\w*)>.*</\2></\1>", label)
#     ret = re.search(r"<(?P<in1>\w+)><(?P<in2>\w+)>\w+</(?P=in2)></(?P=in1)>", label)
#     if ret:
#         print("%s 是符合的标签" % ret.group())
#     else:
#         print("%s 是不符合要求的标签" % label)
#
# # tel = input("输入手机号：")
# ret = re.match(r"^1[3578]\d{9}$", "13658842176")
# if ret is None:
#     print("非法")
# else:
#     print("合理")
#
# # mail = input("输入邮箱：")
# ret = re.match(r"^.+@\w{2,}\.\w{3,}$", "ma@126.com")
# if ret is None:
#     print("不正确")
# else:
#     print("正确")

new_str = re.search(r">([^>]+)<", "<html><table><h1><a>www.itcast.cn</a></h2></table></html>")
# tes = re.match(r"(?<=<(\w+)>).*(?=<(/\1)>)", "<html><table><h1><a>www.itcast.cn</a></h2></table></html>")
print(new_str.group(1))
