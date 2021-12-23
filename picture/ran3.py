import cv2
import numpy as np


if __name__=='__main__':


    img2=cv2.imread('img.png')
    h=img2.shape[0]
    w=img2.shape[1]
    ii=0

    szx=w*3
    szy=h*3

    newimag=np.zeros((szy,szx,3),np.uint8)
    imgx = 0
    imgy = 0

    print(newimag.shape)
    print(range(0,szy))
    for now_y in range(0,szy):
        for now_x in range(0,szx):
            newimag[now_y, now_x, 0] = img2[imgy,imgx,0]
            newimag[now_y, now_x, 1] = img2[imgy,imgx,1]
            newimag[now_y, now_x, 2] = img2[imgy,imgx,2]
            imgx+=1
            if imgx>=w:
                imgx=0
        imgy+=1
        if imgy>=h:
            imgy=0
        # print('.',end='')


    cv2.imshow('newimag',newimag)
    cv2.waitKey()
    cv2.destroyAllWindows()
