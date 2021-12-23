
import cv2
import numpy as np

#图像的纵向镜像的原理是首先获取图像的宽度，将宽度的一半取整之后作为纵向的中线
#以中线为轴，将图像的左边反向复制到右边，使得图像最右边一列的像素等于图像最左边一列的像素。
#横向镜像类似
fn="test1.jpg"

if __name__ == '__main__':

    img = cv2.imread(fn)
    cv2.namedWindow('img')
    cv2.imshow('img', img)
    cv2.waitKey()
    w=img.shape[1]
    h=img.shape[0]
    ii=0
    #关于纵向生成镜像
    #// 与 / 的区别 " / " 表示浮点数除法,返回浮点结果; " // " 表示整数除法
    mirror_w=w//2
    for j in  range(0,h):
        for i in  range(0,mirror_w):
            img[j,i,:]=img[j,w-i-1,:]
        print ('.',end="")
    cv2.namedWindow('img')
    cv2.imshow('img', img)
    cv2.waitKey()
    cv2.destroyAllWindows()
