import sys
from Test import msg

for path in sys.path:
    print(path)

print("修改前的值：", msg.int_, msg.list_)
msg.int_ = 15
msg.list_.append(10)
print("修改后的值：", msg.int_, msg.list_)

import Test.handle
print("被Handle修改后的值：", msg.int_, msg.list_)
print("Handle自己的值：", Test.handle.int_, Test.handle.list_)
