import cv2
import numpy as np

img = cv2.imread('../tool/123.jpg')
print(2.0*img)
new = np.clip(2.0*img-160, 0, 255).astype(np.uint8)
cv2.imwrite('1234.jpg', new)