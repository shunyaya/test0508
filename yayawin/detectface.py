import cv2
from cv2 import imread
from cv2 import cvtColor

img = imread('./camp.jpg')
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faceCascade = cv2.CascadeClassifier('./face_detect.xml')
facerect = faceCascade.detectMultiScale(gray, 1.5, 2)# camp(1.5, 2) twice(1.1, 3)
print(len(facerect))
for(x, y, w, h) in facerect:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)