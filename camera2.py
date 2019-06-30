#!/usr/bin/python3

import cv2
#starting camera 
cap=cv2.VideoCapture(0)
while cap.isOpened():
  status,frame=cap.read()
  #converting image to grayscale
  #cvtColor is used to convert and BGR2GRAY is attribute
  grayimg=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
  #now we can draw all those patterns
  #line
  cv2.line(frame,(4,436),(622,376),(0,255,0),3)
  #rectangle  
  cv2.rectangle(frame,(294,50),(500,300),(0,0,255),3)
  #circle
  cv2.circle(frame,(400,200),120,(255,0,0),3)
  #text
  font=cv2.FONT_HERSHEY_COMPLEX #font which are supported by opencv
  cv2.putText(frame,'mudit',(300,50),font,2,(150,30,255),2,cv2.LINE_AA)
  #here LINE_AA tels that starightline sholud be drawn
  cv2.imshow('live',frame)
  #cv2.imshow('live1',grayimg) 
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
