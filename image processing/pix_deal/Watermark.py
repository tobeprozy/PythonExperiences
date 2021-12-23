import cv2
import numpy as np

if __name__=='__main__':

    img1=cv2.imread('img.png')
    cv2.imshow('preview', img1)
    cv2.waitKey()
    #高表示有多少行像素点，宽表示有多少列像素点
    h=img1.shape[0]
    w=img1.shape[1]
    ii=0
    print(h,w,img1.shape)
    #把三维矩阵分割三个一维矩阵
    r,g,b=cv2.split(img1)
    print(r)
    #将像素点取反
    r=255-r
    b=255-b
    g=255-g
    #将取反的像素返回原来的图像矩阵,必须指定为整数型np.uint8，否则会出现问题
    img2=np.zeros((h,w,3),np.uint8)

    img2[:, :, 0] = r
    img2[:, :, 1] = g
    img2[:, :, 2] = b
    cv2.imshow('preview',img2)
    cv2.waitKey()

    # img3 = img1*0
    # img3[:, :, 0] = r
    # img3[:, :, 1] = g
    # img3[:, :, 2] = b
    # # print(img2==img3)

    # cv2.imshow('preview', img3)
    # cv2.waitKey()

    # cv2.putText(img2,'Machine learning',(0,int(h/2)),cv2.FONT_HERSHEY_PLAIN,2.0,(255,255,255),thickness=2)
    # cv2.imshow('preview',img2)
    # cv2.waitKey()
    #
    # #将图像亮度降为原来的0.8
    # for xi in range(0,w):
    #     for xj in range(0,h):
    #         img1[xj, xi, 0] = int(img1[xj, xi, 0]* 0.8)
    #         img1[xj, xi, 1] = int(img1[xj, xi, 0]* 0.8)
    #         img1[xj, xi, 2] = int(img1[xj, xi, 0]* 0.8)
    #     if xi%10==0:print('.',end='')
    # cv2.imshow('preview',img1)
    # cv2.waitKey()