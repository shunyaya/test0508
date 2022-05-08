import cv2
img = cv2.imread('./original.jpg')
# img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

newimg = img[:150, :200]
#rgb to hsv
# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# cv2.namedWindow('Trackbar')
# cv2.resizeWindow('Trackbar', 640, 320)

# cv2.createTrackbar(' ')

cv2.imshow('newimg', newimg)
cv2.waitKey(0)