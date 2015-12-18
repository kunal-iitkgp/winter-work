	

import cv2
import numpy as np
count_1=0
s_x,s_y,e_x,e_y=0,0,0,0
def draw_path(algo):
     print "ok"
     print "%d %d %d %d" %(s_x,s_y,e_x,e_y)
# mouse callback function

def draw_circle(event,x,y,flags,param):
    global count_1,s_x,s_y,e_x,e_y
    if count_1==2 :
        algo=raw_input("Enter the name of the algo :")
        draw_path(algo)
    elif event == cv2.EVENT_LBUTTONDBLCLK:
        if count_1==0:
            s_x=x
            s_y=y
            cv2.circle(img,(x,y),2,(255,0,0),-1)
            count_1=count_1+1
        elif count_1==1:
            e_x=x
            e_y=y
            cv2.circle(img,(x,y),2,(255,0,0),-1)
            count_1=count_1+1
            
    elif event == cv2.EVENT_RBUTTONDBLCLK:
         
        cv2.circle(img,(x,y),5,(255,255,255),-1)
# Create a black image, a window and bind the function to window
img = np.zeros((500,500,3), np.uint8)
cv2.namedWindow('image',0)
cv2.setMouseCallback('image',draw_circle)

while(1):
    
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()
