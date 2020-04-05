'''
纵向合并所有图片，支持自动判断是否存在子文件夹
'''

import os
from PIL import Image


def is_img(file):  # 判断是否为图片
    filetype = os.path.splitext(file)[1].lower()
    if filetype == '.jpg':
        return True
    elif filetype == '.png':
        return True
    elif filetype == '.jpeg':
        return True
    elif filetype == '.bmp':
        return True
    else:
        return False


def merge(url, target_url, dir_name):
    num = 0  # 统计图片数量
    img_height = 0
    imagefile_list = []
    imagemode_list = []
    for root, dirs, files in os.walk(url):
        for f in sorted(files):
            if is_img(f):  # 筛选所有图片
                num += 1
                img_before = Image.open(os.path.join(url, f))
                img_width = img_before.size[0]
                img_height += img_before.size[1]
                img_open = Image.open(os.path.join(url, f))
                imagemode_list.append(img_open.mode)
                imagefile_list.append(img_open)
                print('第' + str(num) + '图片[' + str(f) + ']成功加入队列')
            else:
                print('[' + str(f) + ']不是图片文件，跳过')
    if len(imagemode_list) > 2:
        print('\n注意：图片色彩模式过多（RGB和CMYK可能共存）')
        in_content = input('是否继续？（请输入y/n）:')
        if in_content == 'y':
            pass
        elif in_content == 'n':
            print('未合并，请检查图片，已结束')
            exit()
    else:
        pass
    print('\n共导入' + str(num) + '张图片，正在合并')

    left = 0
    right = 0
    height = 0
    target = Image.new(img_open.mode, (img_width, img_height))  # 创建新图片尺寸
    for img in imagefile_list:
        height += img.size[1]
        # print(0, right, img.size[0], height)
        target.paste(img, (0, right, img.size[0], height))  # 添加到新图片中
        right += img.size[1]
    target.save(os.path.join(target_url, '合并图片-' + dir_name + '.jpg'), quality=100)  # 保存图片
    return


if __name__ == '__main__':
    # merge(input('请输入图片所在文件夹的父目录：'),input('你想要把图片保存在哪里：'))
    num_finish = 0
    url = input('请输入图片所在文件夹或父文件夹')
    target_url = input('请输入要保存的地址')
    for path, dirs, files in os.walk(url):  # 遍历子文件夹
        if dirs == []:  # 不存在子文件夹，直接对文件进行合并
            print('没有找到子文件夹，将对目前目录下的图片进行合并')
            dir_name = os.path.split(url)[1]
            merge(url, target_url, dir_name)
            num_finish += 1
        else:  # 存在子文件夹，遍历子文件夹中的文件
            for dir in dirs:
                print('正在合并[' + dir + ']文件夹中的图片')
                merge(os.path.join(url, dir), target_url, dir)
                num_finish += 1
                print('第' + str(num_finish) + '个文件夹[' + str(dir) + ']合并完毕')
                print('-' * 20)
            break
    print('合并工作全部结束，共完成' + str(num_finish) + '张图片')
