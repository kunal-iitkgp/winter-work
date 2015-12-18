from numpy import *
from pylab import *

import cv2
# windows to display image
cv2.namedWindow("Color Image")
# read the image
im = cv2.imread('/home/kunal/Desktop/data/pic4.png')
# create a grayscale version
gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
# save the image
cv2.imwrite('/home/kunal/Desktop/data/gray_result.png', gray)
# show image
cv2.imshow("Color Image", im )
# exit at closing of window
cv2.waitKey(0)
cv2.destroyAllWindows()
