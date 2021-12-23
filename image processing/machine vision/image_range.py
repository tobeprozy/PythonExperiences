import cv2
import numpy as np

#采集视频生成视频帧数组
#设置需要采集的视频设备ID为0，从第0个摄像头开始采集
mycap=cv2.VideoCapture(0)
myframe=[]

while True:
    ret,im=mycap.read()
    cv2.imshow("myvideo",im)
    #每15ms采集1次
    myframe.append(im)
    key=cv2.waitKey(150)
    #按空格键推出
    if key==32:
        break
#生成视频帧数组
myframes=np.array(myframe)