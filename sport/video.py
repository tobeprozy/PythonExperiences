# # -*- coding: utf-8 -*-
# """
# Created on Thu Apr 24 12:10:23 2018
#
# @author: irene
# """
#
# import numpy as np
# import matplotlib.pyplot as plt
# import spline
# import math as mt
# import cv2
#
#
# def showpiclocation(img,findimg):
#     #定位图片
#     w=img.shape[1]
#     h=img.shape[0]
#     fw=findimg.shape[1]
#     fh=findimg.shape[0]
#     findpt=None
#     for now_h in range(0,h-fh):
#         for now_w in range(0,w-fw):
#             comp_tz=img[now_h:now_h+fh,now_w:now_w+fw,:]-findimg
#             if abs(np.mean(comp_tz))<20:
#                 findpt=now_w,now_h
#                 print ("ok")
#         print (".",end="")
#     if  findpt!=None:
#         cv2.rectangle(img, findpt, (findpt[0]+fw,findpt[1]+fh),(0,0,255))
#     return img
#
#
# cap = cv2.VideoCapture('1.mp4')  # 读入视频
# myimg1=cv2.imread('12.jpg')
# cv2.imshow('img', myimg1)
# # uing = np.logspace(-3,2,121)
# while (cap.isOpened()):
#     ret, frame = cap.read()
#     # 分解为一帧一帧图像
#     if ret == True:
#         # cv2.imshow("frame"，image)
#         img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 彩色转灰度
#         myimg=showpiclocation(img,myimg1)
#     cv2.imshow('img', myimg)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()
#
# # !/usr/bin/env python
# # -*- coding: utf-8 -*-
# # code:myhaspl@qq.com
# # 10-3.py
# # 少量噪声定位图片

import cv2
import numpy as np

print('loading  ...')


# def showpiclocation(img, findimg):
#     # 定位图片
#     w = img.shape[1]
#     h = img.shape[0]
#     fw = findimg.shape[1]
#     fh = findimg.shape[0]
#     findpt = None
#     for now_h in range(0, h - fh):
#         for now_w in range(0, w - fw):
#             comp_tz = img[now_h:now_h + fh, now_w:now_w + fw, :] - findimg
#             if abs(np.mean(comp_tz)) < 20:
#                 findpt = now_w, now_h
#                 print("ok")
#         print(".", end="")
#     if findpt != None:
#         cv2.rectangle(img, findpt, (findpt[0] + fw, findpt[1] + fh), (0, 0, 255))
#     return img
#
#
#
#
# def addnoise(img):
#     coutn = 50000
#     for k in range(0, coutn):
#         xi = int(np.random.uniform(0, img.shape[1]))
#         xj = int(np.random.uniform(0, img.shape[0]))
#         img[xj, xi, 0] = 255 * np.random.rand()
#         img[xj, xi, 1] = 255 * np.random.rand()
#         img[xj, xi, 2] = 255 * np.random.rand()

def get_EuclideanDistance(x, y):
    myx = np.array(x)
    myy = np.array(y)
    return np.sqrt(np.sum((myx - myy) * (myx - myy)))


def findpic(img, findimg, h, fh, w, fw):
    minds = 1e8
    mincb_h = 0
    mincb_w = 0
    for now_h in range(0, h - fh):
        for now_w in range(0, w - fw):
            my_img = img[now_h:now_h + fh, now_w:now_w + fw, :]
            my_findimg = findimg
            dis = get_EuclideanDistance(my_img, my_findimg)
            if dis < minds:
                mincb_h = now_h
                mincb_w = now_w
                minds = dis
        print(".", end="")
    findpt = mincb_w, mincb_h
    cv2.rectangle(img, findpt, (findpt[0] + fw, findpt[1] + fh), (0, 0, 255))
    return img


def showpiclocation(img, findimg):
    # 定位图片
    w = img.shape[1]
    h = img.shape[0]
    fw = findimg.shape[1]
    fh = findimg.shape[0]
    return findpic(img, findimg, h, fh, w, fw)

fn = '123.png'
fn1 = '12.jpg'
myimg = cv2.imread(fn)
myimg1 = cv2.imread(fn1)
myimg = showpiclocation(myimg, myimg1)


cv2.namedWindow('img')
cv2.imshow('img', myimg)

cv2.waitKey()
cv2.destroyAllWindows()


