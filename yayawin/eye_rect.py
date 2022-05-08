from configparser import Interpolation
import cv2
import numpy as np

def empty(v):
    pass

# reading the image
img = cv2.imread('media\\tzuyu.jpg')

# converting to gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# loading .xml file ?
eye_cascade = cv2.CascadeClassifier('eye_detect.xml')

#　applying the method on gray image
eyes = eye_cascade.detectMultiScale(gray, 1.3, 3)

# newimg = []
print(len(eyes))
if len(eyes)>0:
    for (ex,ey,ew,eh) in eyes:
        # newimg = []
        # cv2.rectangle(img, (ex, ey),(ex+ew, ey+eh), (0, 255, 0), 2)
        print(ex,ey,ew,eh)
        newimg = img[ey:ey+eh, ex:ex+ew]
        newimg = cv2.resize(newimg, (300,300))
        print(newimg) #pixel
        cv2.imshow('newimg', newimg)
        cv2.waitKey(0)
# cv2.imwrite('output.jpg', newimg)



# ---取眼白---
# 1
# converting to hsv
# hsv = cv2.cvtColor(newimg, cv2.COLOR_BGR2HSV)

# making trackbar
cv2.namedWindow('TrackBar')
cv2.resizeWindow('TrackBar', 640, 320)

cv2.createTrackbar('green Min', 'TrackBar', 0, 255, empty)
cv2.createTrackbar('green Max', 'TrackBar', 255, 255, empty)
cv2.createTrackbar('red Min', 'TrackBar', 0, 255, empty)
cv2.createTrackbar('red Max', 'TrackBar', 255, 255, empty)
cv2.createTrackbar('blue Min', 'TrackBar', 0, 255, empty)
cv2.createTrackbar('blue Max', 'TrackBar', 255, 255, empty)

while True:
    g_min = cv2.getTrackbarPos('green Min', 'TrackBar')
    g_max = cv2.getTrackbarPos('green Max', 'TrackBar')
    r_min = cv2.getTrackbarPos('red Min', 'TrackBar')
    r_max = cv2.getTrackbarPos('red Max', 'TrackBar')
    b_min = cv2.getTrackbarPos('blue Min', 'TrackBar')
    b_max = cv2.getTrackbarPos('blue Max', 'TrackBar')
    print(g_min, g_max, r_min, r_max, b_min, b_max)

    lower = np.array([g_min, r_min, b_min])
    upper = np.array([g_max, r_max, b_max])

    mask = cv2.inRange(newimg, lower, upper)
    result = cv2.bitwise_and(newimg, newimg, mask=mask)

    # cv2.imshow('img', img)
    cv2.imshow('grb', newimg)
    cv2.imshow('mask', mask)
    cv2.imshow('reslut', result)
    cv2.waitKey(1)
    # 0 179 2 63 124 238