from turtle import shapesize
import cv2
import numpy as np
img = cv2.imread('media\\yellow.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
print(min(img.flatten()))
# img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
print(gray)
# print(type(gray))
# print(len(gray))
# print(np.size(gray))

# print(hsv)
# print(type(hsv))
# cv2.imshow('hsv', hsv)
# cv2.waitKey(0)

# max_value = None

# for num in gray:
#     if (max_value is None or num > max_value):
#         max_value = num

# print('Maximum value:', max_value)

#rgb to hsv
# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# cv2.namedWindow('Trackbar')
# cv2.resizeWindow('Trackbar', 640, 320)

# cv2.createTrackbar(' ')

# cv2.imshow('newimg', newimg)
# cv2.waitKey(0)