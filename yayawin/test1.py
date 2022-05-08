import cv2

# 圖片
# img = cv2.imread('./original.jpg')
# # cv2.resize(img,(300, 400) ) 調整大小
# cv2.imshow('img', img)
# cv2.waitKey(0)
# 影片

cap = cv2.VideoCapture('./cat.MOV')

# 偵數
while True:
    ret, frame = cap.read()
    cv2.resize(frame, (0, 0), fx=0.2, fy=0.2)
    if ret:
        cv2.imshow('video', frame)
    else:
        break
    if cv2.waitKey(1) == ord('q'):
        break # 按q結束