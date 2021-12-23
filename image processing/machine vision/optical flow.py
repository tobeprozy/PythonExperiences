import cv2
import numpy as  np

def flowdraw (im,flow,step=14):
    #h绘制流光
    h,w=im.shape[:2]
    #reshape( )可以塑形，常见到-1，其作用是当不知道某一维有多少元素时，可先用-1指定，最后由其他维自动计算出来
    y,x=np.mgrid[step/2:h:step,step/2:w:step].reshape(2,-1)
    #上面生成的是浮点数，但是x,y是作为序号的，需要进行强制类型转化为整型
    x=np.array(x,np.int)
    y=np.array(y,np.int)
    fx,fy=flow[y,x].T
    #线终点
    lines=np.vstack([x,y,x+fx,y+fy]).T.reshape(-1,2,2)
    lines=np.int32(lines)
    #创建图像
    myvis=cv2.cvtColor(im,cv2.COLOR_GRAY2BGR)

    for (x1,y1),(x2,y2) in lines:
        cv2.line(myvis,(x1,y1),(x2,y2),(0,255,0),1)
        cv2.circle(myvis, (x1, y1), 1,(0, 255, 0), -1)
    return myvis

#设置需要采集视频设备ID为0，从第0个摄像头采集

mycap=cv2.VideoCapture(0)

#前一个图像
ret,im=mycap.read()

prev_pic=cv2.cvtColor(im,cv2.COLOR_RGB2GRAY)

while True:
    ret, im = mycap.read()
    pic=cv2.cvtColor(im,cv2.COLOR_RGB2GRAY)
    #计算流
    myflow=cv2.calcOpticalFlowFarneback(prev_pic,pic,None,0.5,3,15,3,5,1,0)
    #上帧图像阈值
    # print(myflow[1.0,2.0])
    prev_pic=pic
    #绘制流量矢量
    cv2.imshow("mydiceo flow",flowdraw(pic,myflow,step=14))
    #每15ms采集1次
    key=cv2.waitKey(15)
    #按空格键退出
    if key==32:
        break


