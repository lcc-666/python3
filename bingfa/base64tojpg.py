import base64
import os

"""
base64转jpg
需要提供图片名称,仅支持txt文本文件
可选择提供存储路径（默认当前路径）
"""


def getpic(name, path=r"./"):
    f = open(name, "r")
    txt = f.read().split(',')[-1]
    f.close()
    imgdata = base64.b64decode(txt)
    new_name=name[:3]
    file = open(r"{}.jpg".format(path + new_name), 'wb')
    file.write(imgdata)
    file.close()
    os.remove(name)

if __name__ == '__main__':
    getpic("./a.txt",path=r"C:\Users\admin\Desktop")