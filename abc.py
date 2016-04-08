import numpy as np
import cv2

start_x, start_y = [ int(i) for i in raw_input().strip().split() ]
end_x, end_y = [ int(i) for i in raw_input().strip().split() ]
r,c = [ int(i) for i in raw_input().strip().split() ]

img = cv2.imread("1.png",0)
img = cv2.resize(img, (r,c), interpolation=cv2.INTER_AREA)
ret,img = cv2.threshold(img,127,255,0)
print img[1][1] 
img[1][1] = 0
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()