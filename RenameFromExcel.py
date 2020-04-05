# !/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
excel重命名
第一列为原文件名称
第二列为新文件名称
第三列为准备放入的文件夹名称
右边的名字会替换左边的名字，放入第三列的文件夹中
'''

import os
import os.path
import xlrd
import shutil


def excel_to_json(file_name, read_file_dir):
    data = xlrd.open_workbook(file_name)
    sheet1 = data.sheet_by_index(0)
    nrows = sheet1.nrows  # 行数
    # ncols = sheet1.ncols  # 列数
    # row_data = sheet1.row_values(0)  # 获取第0行的值
    # col_data = sheet1.col_values(0)  # 获取第0列的值
    cell_name_1 = sheet1.cell(0, 0).value  # name_1的值
    cell_name_2 = sheet1.cell(0, 1).value  # name_2的值
    cell_floder_name = sheet1.cell(0, 2).value  # folder的值
    idx = sheet1.row_values(0)
    data = []

    for i in range(1, nrows):
        row_data = sheet1.row_values(i)
        row_data_dict = {}
        for j in range(len(row_data)):
            if isinstance(row_data[j], float):
                item = str(int(row_data[j]))  # 数字转为str
            else:
                item = row_data[j]
            row_data_dict[idx[j]] = item
        data.append(row_data_dict)  # 创建dict
    # print(data)
    # name_json = json.dumps(data, indent=4, ensure_ascii=False)

    files = os.listdir(read_file_dir)  # 列出当前目录下所有的文件
    count_success = 0
    count_failure = 0
    count_folder = 0
    count_file_not_exists = 0
    count_floder_repeat = 0
    count_folder_son = 0
    for num in range(1, nrows):
        try_filename = data[num - 1][cell_name_1]
        if os.path.exists(os.path.join(read_file_dir, try_filename)):  # 检查文件是否存在
            print('找到图片[' + try_filename + ']')
            pass
        else:
            count_file_not_exists += 1
            print('[' + try_filename + ']文件不存在，已跳过', )
            print('-' * 20)
            continue
        for file in files:
            old_name = data[num - 1][cell_name_1]  # 读data的值
            new_name = data[num - 1][cell_name_2]
            folder_name = data[num - 1][cell_floder_name]  # 读新文件夹名字
            if file == old_name:
                filetype = os.path.splitext(file)[1]  # 获取后缀名
                old_path_name = os.path.join(read_file_dir, file)
                new_path_name = os.path.join(read_file_dir, new_name + filetype)
                try:
                    os.rename(old_path_name, new_path_name)  # 重命名
                except:
                    count_failure += 1
                    print("文件重命名失败")
                else:
                    count_success += 1
                    print("第" + str(count_success) + "张图片[" + str(old_name) + ']----->[' + str(new_name) + "]命名完成")
                try:
                    os.mkdir(os.path.join(read_file_dir, folder_name))  # 创建新的文件夹
                except(FileExistsError):
                    count_floder_repeat += 1
                    print('第' + str(count_floder_repeat) + '个文件夹[' + str(folder_name) + ']已经存在')
                except(FileNotFoundError):
                    folder_name_list = folder_name.split('/')
                    for folder_name_little in folder_name_list:
                        try:
                            os.mkdir(os.path.join(read_file_dir, folder_name_little))
                            os.mkdir(os.path.join(read_file_dir, folder_name))
                            count_folder_son += 1
                            print('第' + str(count_folder_son) + '个子文件夹创建成功')
                        except:
                            print('子文件夹创建失败')
                            break
                else:
                    count_folder += 1
                    print('第' + str(count_folder) + '个文件夹[' + str(folder_name) + ']创建完成')
                if os.path.exists(os.path.join(read_file_dir, folder_name)):
                    try:
                        shutil.copy(new_path_name, os.path.join(read_file_dir, folder_name))  # 移动文件夹
                        os.rename(new_path_name, old_path_name)  # 还原文件名称
                        print('成功将图片[' + new_name + ']复制到[' + str(folder_name) + ']文件夹')
                        print('-' * 20)
                    except:
                        print('跳过该图片的移动')
                        print('-' * 20)
                else:
                    print('文件可能已经存在，复制失败')
    print()
    print("共有" + str(count_success) + "张图片命名完成")
    print('共创建了' + str(count_folder) + '个文件夹')
    print("其中" + str(count_failure + count_file_not_exists) + "张图片失败")
    return


if __name__ == '__main__':
    file_name = input("请输入excel文件路径:")
    read_file_dir = input("请输入图片文件夹所在位置:")
    file_name = excel_to_json(file_name,read_file_dir)