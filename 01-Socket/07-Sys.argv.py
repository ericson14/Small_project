import sys

# !/usr/bin/python3
# coding=utf-8
if len(sys.argv)-1 == 0:
    print("Enter exactly one argument")
    exit()
elif len(sys.argv)-1 == 1:
    print("hahaha,{}".format(sys.argv[1]))
elif len(sys.argv)-1 == 2:
    print("{}, hhh, {}".format(sys.argv[1], sys.argv[2]))
else:
    print("Too tired to solve too many arguments")

