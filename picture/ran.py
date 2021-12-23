import cv2
import numpy as np


if __name__=='__main__':
    szx=200
    szy=300
    img=np.zeros((szx,szy,3),np.uint8)

    posx=np.random.randint(200,size=(2000,1))
    posy=np.random.randint(300,size=(2000,1))

    for i in range(2000):
        img[posx[i], posy[i], [0]] = np.random.randint(0,255)
        img[posx[i], posy[i], [1]] = np.random.randint(0, 255)
        img[posx[i], posy[i], [2]] = np.random.randint(0, 255)

    cv2.imshow('preview',img)
    cv2.waitKey()

    img2=cv2.imread('1.png')
    h=img2.shape[1]
    w=img2.shape[0]
    ii=0
    print(w,h,img2.shape)
    for xi in range(0,w):
        for xj in range(0,h):
            img2[xi, xj, 0] = int(img2[xi, xj, 0]*0.8)
            img2[xi, xj, 1] = int(img2[xi, xj, 0] * 0.8)
            img2[xi, xj, 2] = int(img2[xi, xj, 0] * 0.8)
        if xi%10==0:print('.',end='')
    cv2.imshow('preview',img2)
    cv2.waitKey()