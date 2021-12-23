import cv2
import os
import numpy as np

# camera = cv2.VideoCapture(0)

cap = cv2.VideoCapture('1.mp4')  # 读入视频
firstframe = None
i = 0;
while True:
    ret, frame = cap.read()
    if not ret:
        break

    if not os.path.exists('feiji'):
        os.mkdir('feiji')
    cv2.imwrite('feiji/' + str(i) + '.png', frame)
    i=i+1;
    cv2.imshow('img', frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()