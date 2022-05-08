import cv2
import numpy as np

def empty(v):
    pass
img = cv2.imread('./eye.jpg')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


cv2.namedWindow('TrackBar')
cv2.resizeWindow('TrackBar', 640, 320)

cv2.createTrackbar('Hue Min', 'TrackBar', 0, 179, empty)
cv2.createTrackbar('Hue Max', 'TrackBar', 179, 179, empty)
cv2.createTrackbar('Sat Min', 'TrackBar', 0, 255, empty)
cv2.createTrackbar('Sat Max', 'TrackBar', 255, 255, empty)
cv2.createTrackbar('Val Min', 'TrackBar', 0, 255, empty)
cv2.createTrackbar('Val Max', 'TrackBar', 255, 255, empty)


# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
while True:
    h_min = cv2.getTrackbarPos('Hue Min', 'TrackBar')
    h_max = cv2.getTrackbarPos('Hue Max', 'TrackBar')
    s_min = cv2.getTrackbarPos('Sat Min', 'TrackBar')
    s_max = cv2.getTrackbarPos('Sat Max', 'TrackBar')
    v_min = cv2.getTrackbarPos('Val Min', 'TrackBar')
    v_max = cv2.getTrackbarPos('Val Max', 'TrackBar')
    print(h_min, h_max, s_min, s_max, v_min, v_max)

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow('img', img)
    cv2.imshow('hsv', hsv)
    cv2.imshow('mask', mask)
    cv2.imshow('reslut', result)
    cv2.waitKey(1)

cv2.imshow('img', img)
cv2.imshow('hsv', hsv)
cv2.waitKey(0)
# print(img.shape)

# BGR
# 高寬色

# 自製圖片
# img = np.empty((300, 300, 3), np.uint8)
# for row in range(300):
#     for col in range(300):
#         img[row][col] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

# 切割
# newimg = img[:150, 200:400]
# 函式
## 轉灰階
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
##　模糊
# blur = cv2.GaussianBlur(img, (15, 15), 10)
## 邊緣(與周圍像素值差很大)
# canny = cv2.Canny(img, 150, 200)
# ### 膨脹(圖片, 核, iterations)、侵蝕(沒做)
# kernal = np.ones((2, 2), np.uint8)
# dilate = cv2.dilate(canny, kernal, iterations=1)
# cv2.imshow('img', img)
# cv2.waitKey(0)