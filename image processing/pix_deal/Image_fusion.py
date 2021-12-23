#!/usr/bin/env python
# -*- coding: utf-8 -*-

#图像的融合
import cv2
import numpy as np

fn1 = "he.png"
fn2 = "pictestt1.png"
if __name__ == '__main__':
    myimg1 = cv2.imread(fn1)
    myimg2 = cv2.imread(fn2)
    w = myimg1.shape[1]
    h = myimg1.shape[0]
    sz1 = w
    sz0 = h

    # 每个像素为2个像素的平均值
    for y in range(0, sz0):
        for x in range(0, sz1):
            myimg2[y, x, :] = myimg1[y, x, :] * 0.5 + myimg2[y, x, :] * 0.5

            print('.', end="")
    cv2.namedWindow('img2')
    cv2.imshow('img2', myimg2)
    cv2.waitKey()
    cv2.destroyAllWindows()
