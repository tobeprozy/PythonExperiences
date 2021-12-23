#!/usr/bin/env python
# coding=utf-8
# 批量重命名图片名字从-2-01改成-1-01
import os
import time


class ImageRename():
    def __init__(self):
        self.path = './'

    def rename(self):
        filelist = os.listdir(self.path)
        total_num = len(filelist)
        i = 0
        for item in filelist:
            if item[-4:].lower() == '.jpg' or item[-4:].lower() == '.png' or item[-5:].lower() == '.jpeg' or item[
                                                                                                             -4:].lower() == '.gif':
                src = os.path.join(os.path.abspath(self.path), item)
                if "-2-01" in item:
                    rename = item.replace("-2-01", "-1-01")
                    dst = os.path.join(os.path.abspath(self.path), rename)
                    os.rename(src, dst)
                    print('更改图片%s名字中...' % (item))
                    i = i + 1
        if i == 0:
            print("没有符合更改要求的图片名字，程序将在5秒后自动退出！")
        else:
            print('已完成，该目录下共 %d个文件修改了%d张图片，程序将在5秒后自动退出！' % (total_num, i))
        time.sleep(5)


if __name__ == '__main__':
    newname = ImageRename()
    newname.rename()