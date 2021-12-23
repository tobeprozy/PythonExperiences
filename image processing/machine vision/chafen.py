import cv2
import numpy as np
fn=[]
for i in range(6):
    fn.append("mv"+str(i+1)+".png")

print(fn)

img=[]
colorimg=[]
myimg=[]

for i in range(6):
    tmpimg=(cv2.imread(fn[i]))
    colorimg.append(tmpimg)
    myimg=cv2.cvtColor(tmpimg,cv2.COLOR_BGR2GRAY)
    img.append(myimg)

myimg1=colorimg[0].copy()
myimg2=myimg1.copy()

w=myimg1.shape[1]
h=myimg1.shape[0]

moveimg1=np.zeros((h,w),np.uint8)
moveimg2=np.zeros((h,w,3),np.uint8)

for ii in range(5):
    print("开始分析第"+str(ii)+"个运动图像")
    myd=img[ii+1]-img[ii]
    #生成差分矩阵
    threshold=int(np.median(abs(myd)))#取中位数作为阈值
    mymove=np.ones([h,w],np.uint8)

    for i in range(h):
        for j in range(w):
            if abs(myd[i,j])<threshold or myd[i,j]==0:
                mymove[i,j]=0
    #如果有物体运动则输出报警，并生成运动效果叠加图
    if np.sum(mymove)>0:
        print("第"+str(ii)+"个运动图像发生变化了")
        moveimg1=img[ii+1]*(1-mymove)*0.16+img[ii]*(1-mymove)*0.16+moveimg1
        moveimg2=colorimg[ii+1]*0.16+colorimg[ii]*0.16+moveimg2
        moveimg1=np.array(moveimg1,np.uint8)
        moveimg2=np.array(moveimg2, np.uint8)

#显示运动画面
#计算运动部分

moveimg1=moveimg1-img[0]
retval,showimg1=cv2.threshold(moveimg1,140,255,cv2.THRESH_BINARY)
showimg1=showimg1
showimg2=moveimg2

cv2.imshow("move1",showimg1)
cv2.imshow("move2",showimg2)
cv2.waitKey()
cv2.destroyAllWindows()
