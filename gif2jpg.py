'''
gif图批量转存为jpg图片
'''

import os
from PIL import Image


def change(url, folder):
    for path, dirs, files in os.walk(url):  # 遍历所有子文件
        for file in sorted(files):
            gif_url = os.path.join(url, file)
            file_name = str(file).split('.')[0]
            jpg_url = os.path.join(folder, file_name + '.jpg')
            im = Image.open(gif_url)
            background = Image.new("RGB", im.size, (255, 255, 255))
            background.paste(im)
            background.save(jpg_url, 'JPEG', quality=100)
            print('jpg文件写入成功：' + file_name)


def make_file(url):
    file_name = str(url).split('/')[-1]
    result_url = input('输入存放地址文件夹：') # 目标文件夹
    folder = os.path.join(result_url, file_name)
    try:
        os.makedirs(folder)  # 创建同名文件
    except:
        print('文件已经存在，将直接存入该文件夹')
        pass
    return folder


if __name__ == '__main__':
    # 输入gif所在地址
    url = input('输入gif源文件所在地址：')
    folder = make_file(url)
    change(url, folder)
