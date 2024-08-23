"""
TODO 通过递归找出一个文件夹内的全部文件
思路：写一个函数，列出文件夹内全部内容，如果是文件就收集到list
如果是文件夹，就递归调用自己，再次判断
"""

import os

def test_os():
    # 演示os模块的三个用法
    print(os.listdir("文件路径"))  #列出指定文件夹中有哪些内容
    print(os.path.isdir("文件路径"))  #判断这个路径是不是文件夹
    print(os.path.exits("文件路径"))  #判断这个文件夹是否存在

def get_files_recuriosn_from_dir(path):
    """
    从指定的文件夹中使用递归的方式，获取全部的文件列表
    :param path:被判断的文件夹
    :return:list。包含全部的文件，如果目录不存在或者无文件返回一个空的list
    """
    print(f'当前判断的文件夹是，{path}')
    file_list = []
    if os.path.exists(path):
        for f in os.listdir(path):
            new_path = path + "/" + f
            if os.path.isdir(new_path):
                file_list += get_files_recuriosn_from_dir(new_path)  #+=递归调用自己的返回值传递进行累积
            else:
                file_list.append(new_path)
    else:
        print(f"指定的目录{path}不存在")
        return []

    return file_list

if __name__ == '__main__':
    print(get_files_recuriosn_from_dir("文件路径"))