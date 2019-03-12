#  _*_ coding:utf-8 _*_
#  QQ: 2457179751
__author__ = 'xmduke'
"""
对于超大文件建议用逐行或分块的方式处理；逐行处理可能慢一些，但编码更简单清晰一点；上面给出的是按分块方式处理的

如下:
"""

import linecache
import random
import sys
import os

class r_title(object):
    def getfilelines(filename, eol='\n', buffsize=4096):
        """计算给定文件有多少行"""
        with open(filename, 'rb') as handle:
            linenum = 0
            buffer = handle.read(buffsize)
            while buffer:
                linenum += buffer.count(eol.encode()) # 需要加上 encode() ，不然会报错:TypeError: a bytes-like object is required, not 'str' ,报错原因：在这里，python3和Python2在套接字返回值解码上有区别。
                buffer = handle.read(buffsize)
            return linenum


    def readtline(filename, lineno, eol="\n", buffsize=4096):
        """读取文件的指定行"""
        with open(filename, 'rb') as handle:
            readedlines = 0
            buffer = handle.read(buffsize)
            while buffer:
                thisblock = buffer.count(eol.encode())
                if readedlines < lineno < readedlines + thisblock:
                    # inthisblock: findthe line content, and return it
                    return buffer.split(eol.encode())[lineno - readedlines - 1]
                elif lineno == readedlines + thisblock:
                    # need continue read line rest part
                    part0 = buffer.split(eol.encode())[-1]
                    buffer = handle.read(buffsize)
                    part1 = buffer.split(eol.encode())[0]
                    return part0 + part1
                readedlines += thisblock
                buffer = handle.read(buffsize)
            else:
                raise IndexError


    def getrandomline(filename):
        """读取文件的任意一行"""
        import random
        return r_title.readtline(filename,random.randint(0, r_title.getfilelines(filename)),).decode('gbk')


# if __name__ == "__main__":
#     if len(sys.argv) == 1:
#         #r_title.getrandomline("title.csv")
#         print(r_title.getrandomline("title.csv"))
#     else:
#         for f in filter(os.path.isfile, sys.argv[1:]):
#             print(r_title.getrandomline(f))


