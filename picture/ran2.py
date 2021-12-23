import cv2
import numpy as np


if __name__=='__main__':

    img2=cv2.imread('img.png')
    h=img2.shape[0]
    w=img2.shape[1]
    ii=0
    print(h,w,img2.shape)
    r,g,b=cv2.split(img2)
    print(r)
    r=255-r
    b=255-b
    g=255-g

    img2[:,:,0]=r
    img2[:, :, 1] = g
    img2[:, :, 2] = b
    cv2.imshow('preview',img2)
    cv2.waitKey()

    cv2.putText(img2,'Machine learning',(0,int(h/2)),cv2.FONT_HERSHEY_PLAIN,2.0,(255,255,255),thickness=2)
    cv2.imshow('preview',img2)
    cv2.waitKey()
    for xi in range(0,w):
        for xj in range(0,h):
            img2[xj, xi, 0] = int(img2[xj, xi, 0]*0.8)
            img2[xj, xi, 1] = int(img2[xj, xi, 0]* 0.8)
            img2[xj, xi, 2] = int(img2[xj, xi, 0] * 0.8)
        if xi%10==0:print('.',end='')
    cv2.imshow('preview',img2)
    cv2.waitKey()