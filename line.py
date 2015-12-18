import numpy as np
import cv2

# Create a black image
img = np.zeros((100,100,3), np.uint8)

cv2.namedWindow('image',0)
# Draw a diagonal blue line with thickness of 5 px

cv2.line(img,(20,20),(21,21),(255,0,0),1)
cv2.line(img,(20,20),(21,20),(255,0,0),1)
cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
