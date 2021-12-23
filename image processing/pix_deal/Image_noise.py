
import cv2
import numpy as np
#t
fn="test1.jpg"
if __name__ == '__main__':

    img = cv2.imread(fn)
    coutn=100000
    for k in range(0,coutn):
	    xi = int(np.random.uniform(0,img.shape[1]))
	    xj = int(np.random.uniform(0,img.shape[0]))
	    if img.ndim == 2:
            # 灰色图像加噪
		    img[xj,xi] = 255
	    elif img.ndim == 3:
            #彩色图像加噪
		    img[xj,xi,0]= 25
		    img[xj,xi,1]= 20
		    img[xj,xi,2]= 20
    cv2.namedWindow('img')
    cv2.imshow('img', img)
    cv2.waitKey()
    cv2.destroyAllWindows()
