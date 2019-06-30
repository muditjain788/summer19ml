import cv2
import sys
data=sys.argv[1]
img=cv2.imread(data,1)
img1=cv2.imread(data,0)
print(img)
cv2.imshow('windowname',img)
cv2.imwrite('dog.jpg',img1)
cv2.waitKey(0)

