import cv2
import matplotlib.pyplot as plt
import numpy as np


cap = cv2.VideoCapture(0)   
while(True):
    ret, frame = cap.read()
    
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lwr=np.array([150,50,50])
    upr=np.array([180,255,255])
    mask=cv2.inRange(hsv,lwr,upr)
    
    redseg=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow("redframe",redseg)
    cv2.imshow("og",frame)
    cv2.imshow("mask",mask)
    if cv2.waitKey(1) & 0xFF == ord('p'):
        break

cap.release() 
cv2.destroyAllWindows()
