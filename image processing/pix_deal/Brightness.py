
#-*- coding: utf-8 -*-

import cv2

fn="test1.jpg"
if __name__ == '__main__':

    print ('loading %s ...' % fn)
    print (u'正在处理中',)
    img = cv2.imread(fn)
    w=img.shape[1]
    h=img.shape[0]
    ii=0
    #将全部色彩变暗
    for xi in range(0,w):
        for xj in range (0,h):
            img[xj,xi,0]= int(img[xj,xi,0]*0.2)
            img[xj,xi,1]= int(img[xj,xi,1]*0.2)
            img[xj,xi,2]= int(img[xj,xi,2]*0.2)
        if  xi%10==0 :print( '.', end="" )
    cv2.namedWindow('img')
    cv2.imshow('img', img)
    cv2.waitKey()
    cv2.destroyAllWindows()
    print('')
    print (u'正在处理中' ,  )
    #将全部色彩变亮
    for xi in range(0,w):
        for xj in range (0,h):
            img[xj,xi,0]= int(img[xj,xi,0]*10.2)
            img[xj,xi,1]= int(img[xj,xi,1]*10.2)
            img[xj,xi,2]= int(img[xj,xi,2]*10.2)
        if  xi%10==0 :print( '.', end="" )
    cv2.namedWindow('img')
    cv2.imshow('img', img)
    cv2.waitKey()
    cv2.destroyAllWindows()
