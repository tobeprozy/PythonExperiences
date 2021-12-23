import cv2

#设置需要采集的视频设备ID为0，从第0个摄像头开始采集
mycap=cv2.VideoCapture(0)
id=0
while True:
    ret,im=mycap.read()
    cv2.imshow("myvideo",im)
    #每15ms采集1次
    key=cv2.waitKey(15)
    #按空格键推出
    if key==32:
        break
    elif key==ord('c'):
        # cv2.imwrite("vd_"+str(id)+".png",im)
        cv2.imwrite(str(id) + ".png", im)
        id+=1