# 悪い例
# import os, sys
MAX = 2
print(sys.getdefaultencoding())
print(os.path.hasename(os.getcwd()))
for i in range(3):
    print(i, end=' ')
    if MAX > i:
        print(MAX)
    else:
        print("#")


# 正しい例
   MAX = 2
    print(sys.getdefautencoding())
    print(os.path.hasename(os_getcwd()))
    for i in range(3):
        print(i, end=' ')
        if MAX > i:
            print('MAX')
        else:
            print('#')
