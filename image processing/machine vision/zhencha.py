import cv2
import numpy as np

fn=[]
for i in range(6):
    fn.append("mv"+str(i+1)+".png")

img=[]
colorimg=[]
myimg=[]

for i in range(6):
    tmpimg=cv2.imread(fn[i])
    colorimg.append(tmpimg)
    myimg=cv2.cvtColor(tmpimg,cv2.COLOR_BGR2GRAY)
    img.append(myimg)

myimg=colorimg[0].copy()
w=myimg.shape[1]
h=myimg.shape[0]

moveimg=np.zeros((h,w,3),np.uint8)

for ii in range(5):
    print("开始分析第" + str(ii) + "个运动图像")
    myd = img[ii + 1] - img[0]
    # 生成差分矩阵
    threshold = int(np.median(abs(myd)))  # 取中位数作为阈值
    mymove = np.ones([h, w], np.uint8)

    for i in range(h):
        for j in range(w):
            if abs(myd[i, j]) < threshold or myd[i, j] == 0:
                mymove[i, j] = 0
    # 如果有物体运动则输出报警，并生成运动效果叠加图
    if np.sum(mymove) > 0:
        print("第" + str(ii) + "个运动图像发生变化了")
        moveimg = colorimg[ii + 1]  * 0.16 + colorimg[ii] *  0.16 + moveimg
        moveimg = np.array(moveimg, np.uint8)


# 显示运动画面



showimg= moveimg
cv2.imshow("showimg", showimg)
cv2.waitKey()
cv2.destroyAllWindows()


