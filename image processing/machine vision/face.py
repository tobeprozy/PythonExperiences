import cv2

# 读取图片
img = cv2.imread("facesb.png")
# 加载模型，模型可以从https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml下载
classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# 人脸检测
# scaleFactor：两次相邻的检测中，搜索窗口扩大的比例系数
# minNeighbors：表示构成检测目标的相邻矩形的最小个数，默认为3，即相邻的检测中，至少有三次检测判断为真，才算真的目标
# minSize：检测目标的最小尺寸
faces = classifier.detectMultiScale(img, scaleFactor=1.1, minNeighbors=3, minSize=(32, 32))
for face in faces:
    x, y, w, h = face
    # 绘制边框
    cv2.rectangle(img, (x, y), (x + h, y + w), (0, 255, 0), 2)
if len(faces) > 0:
    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()