# -*- coding: utf-8 -*-

'''
把指定目录下的文件夹依次打包成zip压缩文件
并且放入目标文件夹
'''
import os
import shutil


def make_zip(dir_url, target_url):
    if dir_url == target_url:
        print('处理路径和目标路径不可以相同！请重新输入')
    else:
        count_zip = 0
        os.chdir(dir_url)
        print('正在操作的路径为:' + os.getcwd())  # 返回当前操作目录
        print('-' * 20)
        for file in os.listdir():  # 列出所有文件夹
            print('正在处理:[' + file + ']······')
            if os.path.isdir(os.path.join(dir_url, file)):
                shutil.make_archive(os.path.join(target_url, file), 'zip', root_dir=os.path.join(dir_url, file))
                count_zip += 1
                # print(os.path.join(target_url,file))
                # print(os.path.join(dir_url,file))
                print('第' + str(count_zip) + '个文件夹[' + str(file) + ']压缩完成')
                print('-' * 20)
            else:
                print('[' + file + ']不是文件夹，跳过')
                print('-' * 20)
        print('全部完成')
    return


if __name__ == '__main__':
    # dir_url = make_zip(input("请输入文件夹所在位置:"), input('请输入放置的目标位置:'))
    dir_url = make_zip('/Users/hunliji/Desktop/婚礼纪-可蒙/造梦家/20200217 造梦家批处理/成品/jpg-城市分组',
                       '/Users/hunliji/Desktop/婚礼纪-可蒙/造梦家/20200217 造梦家批处理/设计稿/所有jpg按城市分别压缩')
