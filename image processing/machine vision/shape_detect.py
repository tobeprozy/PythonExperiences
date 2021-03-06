import cv2
import numpy as np


#形状检测

def mydist(point1,point2):
    return np.sqrt(np.power((point1[0]-point2[0]),2)+np.power((point1[1]-point2[1]),2))

#离中心点距离的标准差
def getstd(tmpimg,centerpoint):
    w=tmpimg.shape[1]
    h=tmpimg.shape[0]
    dst=[]
    for i in range(h):
        for j in range(w):
            if tmpimg[i,j]<255:
                #该像素点不是空白，是线条中的点
                dst.append(mydist((i,j),centerpoint))
    mysd=np.std(dst)
    return mysd
#读取样本形状图像，计算标准差
imgsd=[]
testimgsd=[]
mysdratio=[]

centerpoint=(26,26)
for i in range(3):
    tmpimg=(cv2.imread("shape"+str(i)+".png"))
    myimg=cv2.cvtColor(tmpimg,cv2.COLOR_BGR2GRAY)
    retval,newimg=cv2.threshold(myimg,40,255,cv2.THRESH_BINARY)
    myimg=cv2.resize(newimg,(51,51))
    imgsd.append(getstd(myimg,centerpoint))

print("***********************************")

for i in range(4):
    #测试样本
    fn="shapetest_"+str(i)+".png"
    tmpimg=(cv2.imread(fn))
    myimg=cv2.cvtColor(tmpimg,cv2.COLOR_BGR2GRAY)
    retval,newimg=cv2.threshold(myimg,40,255,cv2.THRESH_BINARY)
    myimg=cv2.resize(newimg,(51,51))
    #得到距离标准差
    testimgsd.append(getstd(myimg,centerpoint))
    mysdratio.append([])
    for ii in range(3):
        #与样本进行比较
        mysdratio[i].append(abs(testimgsd[i]-imgsd[ii]))

print("KNN距离矩阵如下:")
print(mysdratio)
print("***********")
#KNN算法找邻近

for i in range(4):
    fn="shapetest_"+str(i)+".png"
    myindex=0
    mymin=np.min(mysdratio[i])
    for ii in range(3):
        #测试样本最终分类
        if (mysdratio[i][ii])==mymin:
            myindex=ii
            break
    print(fn+"分类为:"+str(myindex))



