
import cv2
import numpy as np


#图像边缘算法

fn = "Edge_algorithm.jpg"

#计算图像的欧氏距离
def get_EuclideanDistance(x, y):
    myx = np.array(x)
    myy = np.array(y)
    return np.sqrt(np.sum((myx - myy) * (myx - myy)))


if __name__ == '__main__':

    myimg1 = cv2.imread(fn)
    w = myimg1.shape[1]
    h = myimg1.shape[0]
    sz1 = w
    sz0 = h

    # 创建空白图像
    myimg2 = np.zeros((sz0, sz1, 3), np.uint8)
    # 对比产生线条
    black = np.array([0, 0, 0])
    white = np.array([255, 255, 255])
    centercolor = np.array([125, 125, 125])
    for y in range(0, sz0 - 1):
        for x in range(0, sz1 - 1):

            mydown = myimg1[y + 1, x, :]
            myright = myimg1[y, x + 1, :]

            myhere = myimg1[y, x, :]
            lmyhere = myhere
            lmyright = myright
            lmydown = mydown
            if get_EuclideanDistance(lmyhere, lmydown) > 16 and get_EuclideanDistance(lmyhere, lmyright) > 16:
                myimg2[y, x, :] = black
            elif get_EuclideanDistance(lmyhere, lmydown) <= 16 and get_EuclideanDistance(lmyhere, lmyright) <= 16:
                myimg2[y, x, :] = white
            else:
                myimg2[y, x, :] = centercolor

            print
            '.',

    cv2.namedWindow('img2')
    cv2.imshow('img2', myimg2)
    cv2.waitKey()
    cv2.destroyAllWindows()
