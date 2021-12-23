import cv2
import numpy as np
import glob
# 设置寻找亚像素角点的参数，采用的停止准则是最大循环次数30和最大误差容限0.001
criteria = (cv2.TERM_CRITERIA_MAX_ITER | cv2.TERM_CRITERIA_EPS, 30, 0.001)
# 获取标定板角点的位置
w=7
h=9
objp = np.zeros((w * h, 3), np.float32)
objp[:, :2] = np.mgrid[0:w, 0:h].T.reshape(-1, 2) # 将世界坐标系建在标定板上，所有点的Z坐标全部为0，所以只需要赋值x和y
obj_points = [] # 存储3D点
img_points = [] # 存储2D点
images = glob.glob("camera/*.bmp")
for fname in images:
  print(fname)
  img = cv2.imread(fname)
  cv2.imshow('img',img)
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  size = gray.shape[::-1]
  ret, corners = cv2.findChessboardCorners(gray, (w, h))
  print(ret)
  if ret:
    obj_points.append(objp)
    corners2 = cv2.cornerSubPix(gray, corners, (5, 5), (-1, -1), criteria) # 在原角点的基础上寻找亚像素角点
    #print(corners2)
    if [corners2]:
      img_points.append(corners2)
    else:
      img_points.append(corners)

    cv2.drawChessboardCorners(img, (w, h), corners, ret) # 记住，OpenCV的绘制函数一般无返回值
    cv2.imshow('img', img)
    cv2.waitKey(2000)
cv2.destroyAllWindows()
print(len(img_points))

# 标定
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(obj_points, img_points, size, None, None)
print("ret:", ret)
print("mtx:\n", mtx) # 内参数矩阵
print("dist:\n", dist) # 畸变系数  distortion cofficients = (k_1,k_2,p_1,p_2,k_3)
print("rvecs:\n", rvecs) # 旋转向量 # 外参数
print("tvecs:\n", tvecs ) # 平移向量 # 外参数
print("-----------------------------------------------------")