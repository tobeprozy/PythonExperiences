# coding=utf-8
import urllib
import urllib.request
from urllib.parse import quote
import re
import os

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
}
print("****************************************************************************************")
keyword = input("请输入要下载的图片：")
last_dir = "D://python/project/first/pa/test01"
dir = "D://python/project/first/pa/test01//" + keyword
if os.path.exists(last_dir):
    if os.path.exists(dir):
        print("文件夹已经存在")
    else:
        os.mkdir(dir)
        print(dir + "已经创建成功")
else:
    os.mkdir(last_dir)
    if os.path.exists(dir):
        print("文件夹已经存在")
    else:
        os.mkdir(dir)
        print(dir + "已经创建成功")
keyword1 = quote(keyword, encoding="utf-8")
url = "https://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=" + keyword1
req = urllib.request.Request(url, headers=headers)
f = urllib.request.urlopen(req).read().decode("utf-8")
key = r'thumbURL":"(.+?)"'
key1 = re.compile(key)
num = 0



for string in re.findall(key1,f):
    print("正在下载" + string)
    f_req = urllib.request.Request(string, headers=headers)
    f_url = urllib.request.urlopen(f_req).read()
    fs = open(dir + "/" + keyword + str(num) + ".jpg", "wb+")
    fs.write(f_url)
    fs.close()
    num += 1
    print(string + "已下载成功")


input("按任意键结束程序：")