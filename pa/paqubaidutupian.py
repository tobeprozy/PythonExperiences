# coding=utf-8
import urllib
import urllib.request
from urllib.parse import quote
import re
import os

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.52"
}

url = "https://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%E7%BE%8E%E5%A5%BD"
req = urllib.request.Request(url, headers=headers)
f = urllib.request.urlopen(req).read().decode("utf-8")

print(url)
print(f)
