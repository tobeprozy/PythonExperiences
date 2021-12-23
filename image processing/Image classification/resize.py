
import cv2

img = cv2.imread("ptest1.png")
img = cv2.resize(img, (800, 600), interpolation=cv2.INTER_AREA)
cv2.imshow("nihao",img)
cv2.waitKey()