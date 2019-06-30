#!/usr/bin/python3

import cv2
#starting camera 
cap=cv2.VideoCapture(0)# 0 means which cammera mean default cameraa if tehree is another cammera than 1
if cap.isOpened() :
   print("cameraa is ready to take pictures")
else:
   print("otherwise check your webcam driverss")

#now we can read input from camera
status,img=cap.read() #it will take first picture it clicks the picture
status1,img1=cap.read()
#now showing
cv2.imshow('liveimage',img)
cv2.imshow('liveshow',img1)
cv2.waitKey(0)
#to close camera
cap.release()
