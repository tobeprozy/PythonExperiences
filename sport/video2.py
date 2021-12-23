import cv2
import numpy as np

# camera = cv2.VideoCapture(0)

cap = cv2.VideoCapture('1.mp4')  # 读入视频
firstframe = None
while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)


    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()