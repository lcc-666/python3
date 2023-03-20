import os
from PIL import Image
import shutil
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

"""
将图片按照横竖屏来分类
"""


def getsize(i):
    img = Image.open(i)
    w = img.width
    h = img.height
    if w > h:
        shutil.move(i, './width')
    else:
        shutil.move(i, './heigth')


def main(path):
    start = time.time()
    file = path
    ls = os.listdir(file)
    os.mkdir('./width')
    os.mkdir('./heigth')
    # for i in ls:
    #     getsize(file+i)
    with ThreadPoolExecutor(max_workers=128) as executor:
        future_list = []
        for i in ls:
            future = executor.submit(getsize, file + i)
            future_list.append(future)
        as_completed(future_list)
    end = time.time()
    print(end - start)


main("/home/chaoge/Downloads/赛尔号/")
