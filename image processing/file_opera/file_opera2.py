
import os
# 引入shutil模块
import shutil
# 复制或移动到目的文件夹下面
# 如果只写目标文件夹的名称的话，如果目标文件夹不存在，则会将复制或移动之后的文件重命名为目标文件夹的名称
# demo.txt 复制到 新的文件夹 下面
open("demo.txt", 'w')
shutil.copy('demo.txt','新的文件夹')
# file1.txt 移动到 新的文件夹 下面
open("file1.txt", 'w')
shutil.move('file1.txt','新的文件夹')
# 复制或移动到目的文件夹下面之后，重命名
# 如果目标文件夹不存在，则会报错
# demo.txt 复制到 新的文件夹 下面，并重命名为new1.txt
shutil.copy('demo.txt','新的文件夹/new1.txt')
# file2.txt 移动到 新的文件夹 下面，并重命名为 new2.txt
open("file2.txt", 'w')
shutil.move('file2.txt','新的文件夹/new2.txt')