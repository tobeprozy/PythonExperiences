# -*- coding: utf-8 -*-


#最简单的批处理修改名字的办法
import os
import shutil
def rename(path):
    files = os.listdir(path)
    print(files)
    count=1
    for i in files:
        print(os.path.join(path+"/"+i))
        os.rename(os.path.join(path+"/"+i),os.path.join(path+"/food"+str(count)+".jpg"))
        count+=1

if __name__ == '__main__':
    # path="D:\\python\project\\first\\image processing\\Batch\\pic"  #正确
    path = "C:/Users/南叔先生/Desktop/Sort_1000pics-2/test/食物"       #正确
    # path = "D:\python\project\first\image processing\Batch\pic"     #错误的路径
    rename(path)