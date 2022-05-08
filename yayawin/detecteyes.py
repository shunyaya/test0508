import cv2
from cv2 import imread

eye_cascade = cv2.CascadeClassifier('./eye_detect.xml')
# cv2.data.haarcascades + 

img = imread('./tzuyu.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
eyes = eye_cascade.detectMultiScale(gray, 1.3, 3)
print(len(eyes))

for (ex,ey,ew,eh) in eyes:
    #for i in range(len(eyes)):
    cv2.rectangle(img, (ex, ey),(ex+ew, ey+eh), (0, 255, 0), 2)
    print(ex,ey,ew,eh)

cv2.imshow('img', img)
cv2.waitKey(0)

# newimg = img[ex-eh:ex+ew,ex-eh:ey]
# cv2.imshow('newimg', newimg)

# ---
# def detect(filename):
#     img = cv2.imread(filename)
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=3)
#     for (x,y,w,h) in faces:
#         roi_gray = gray[y:y+h, x:x+w]
#         eyes = eye_cascade.detectMultiScale(roi_gray,scaleFactor=1.02, minNeighbors=3, minSize=(40,40),)
#         img = cv2.rectangle(img, (x,y), (x+w,y+h), (255, 0, 0), 2)
#         for (ex,ey,ew,eh) in eyes:
#             img = cv2.rectangle(img,(x+ex,y+ey),(x+ex+ew,y+ey+eh),(0,255,0),2)
#     cv2.imwrite('./camp.jpg', img)
 
# detect('./camp.jpg')

# cv2.imshow('./camp.jpg')