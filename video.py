#!/usr/bin/python3

import cv2
#starting camera 
cap=cv2.VideoCapture(0)
#loading plugin
plugin=cv2.VideoWriter_fourcc(*'XVID')#adding plugin xvid supports mp4 and avi
#jis naame se save , ,speed,framesize
output=cv2.VideoWriter('class.avi',plugin,20,(640,480))#saving video 

while cap.isOpened():
  status,frame=cap.read()
  cv2.imshow('live',frame)
  #you can draw patterns if want
  output.write(frame)
  if cv2.waitKey(10) & 0xff ==ord('q') :
    break
cv2.destroyAllWindows() #to destroy all windows
#to close camera
cap.release()
