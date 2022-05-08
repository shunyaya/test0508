# ---取眼白---
# 2
import cv2
from cv2 import imread
import numpy as np

newimg = imread('./output.jpg')

newimg1 = newimg*0.8
newimg1[newimg1 > 255] = 255
newimg1 = np.round(newimg1)
newimg1 = newimg1.astype(np.uint8)

cv2.imshow('newimg1', newimg1)
cv2.waitKey(0)

imgContour = newimg1.copy()
newimg1 = cv2.cvtColor(newimg1, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(newimg1, 80, 150)
contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

for cnt in contours:
    cv2.drawContours(newimg, cnt, -1, (255, 0, 0), 2)
    cv2.imshow('newimg1', newimg)
# cv2.imshow('canny', canny)
# cv2.imshow('imgContour', imgContour)
    cv2.waitKey(0)