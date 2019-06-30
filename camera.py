#!/usr/bin/python3

import cv2
#starting camera 
cap=cv2.VideoCapture(0)
while cap.isOpened():
  status,frame=cap.read()
  #converting image to grayscale
  #cvtColor is used to convert and BGR2GRAY is attribute
  grayimg=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
  cv2.imshow('live',frame)
  cv2.imshow('live1',grayimg) 
  if cv2.waitKey(10) & 0xff == ord('q'):
    break
# oxff is ascii detector in python and now python don't understand whaat is q
#so we applied ord function to change q in ascii format
#whenwever it is 10 seconds and we press q just stop
#humne mouse se ched diya to contro mouse ke passs cha jeayega jisse niche wale #function kam nahi karenge to hum kuch alg karna padega




#v2.destroywindow('live')
cv2.destroyAllWindows() #to destroy all windows
#to close camera
cap.release()
