from PIL import Image, ImageDraw, ImageFont
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import tqdm

"""
批量给图片添加水印
"""


# 创建一个文件夹啊存储修改后的图片
def mkdir():
    try:
        os.mkdir('./new')
    except FileExistsError:
        print("文件夹创建成功")


# 获取当前目录的所有JPG文件
def get_list():
    jpg_list = []
    ls = os.listdir('./')
    for i in ls:
        if i.split('.')[-1] == 'jpg':
            jpg_list.append("./" + i)
    return jpg_list


# 加水印
def made(file):
    try:
        savename = file.split('/')[-1]
        txt = savename.split('.')[0]
        img = Image.open(file)
        w, h = img.size
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('simsun.ttc', size=20, encoding='utf-8')
        txtW, txtH = draw.textsize(txt, font=font)
        draw.text((w - txtW, h - txtH - 5), text=txt, fill=(20, 192, 192, 192), font=font, )
        img.save('./new/' + savename)
        os.remove(file)
    except:
        pass


def main():
    start = time.time()
    mkdir()
    ls = get_list()
    # 多线程操作
    with ThreadPoolExecutor(max_workers=16) as executor:
        # 列表用于存储线程
        future_list = []
        results = []
        for i in ls:
            # 使用submit提交函数和参数并存储到列表中
            future = executor.submit(made, i)
            future_list.append(future)
        # tqdm添加进度条
        for task in tqdm.tqdm(as_completed(future_list), total=len(future_list)):
            results.append(task.result())
    end = time.time()
    data = end - start
    print('%.2f' % data)


if __name__ == '__main__':
    main()
