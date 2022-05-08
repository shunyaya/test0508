import cv2
from cv2 import imread
from cv2 import resize
import numpy as np


# def show(final):
#     print('display')
#     cv2.imshow('Temple', final)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

img = imread('media\\tzuyu.jpg')

def eyeimg(img):

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # converting to gray
    eye_cascade = cv2.CascadeClassifier('eye_detect.xml') # loading .xml file
    eyes = eye_cascade.detectMultiScale(gray, 1.3, 3)  #　applying the method on gray image
    print(len(eyes))
    for (ex,ey,ew,eh) in eyes:
        print(ex,ey,ew,eh)
        newimg = img[ey:ey+eh, ex:ex+ew]
        newimg = resize(newimg, (0, 0), fx=2, fy=2)
        print(newimg) #pixel
        cv2.imshow('newimg', newimg)
        cv2.waitKey(0)
    
    result = cv2.cvtColor(newimg, cv2.COLOR_BGR2LAB)
    avg_a = np.average(result[:, :, 1])
    avg_b = np.average(result[:, :, 2])
    for x in range(result.shape[0]):
        for y in range(result.shape[1]):
            l, a, b = result[x, y, :]
            l *= 100 / 255.0
            result[x, y, 1] = a - ((avg_a - 128) * (l / 100.0) * 1.1)
            result[x, y, 2] = b - ((avg_b - 128) * (l / 100.0) * 1.1)
    result = cv2.cvtColor(result, cv2.COLOR_LAB2BGR)
    print(result) #pixel
    cv2.imshow('result', result)
    cv2.waitKey(0)
    
    # return result


eyeimg(img)

# final = np.hstack((img, eyeimg(img)))
# show(final)
# cv2.imwrite('result.jpg', final)

# def white_balance_loops(img):
#     result = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
#     avg_a = np.average(result[:, :, 1])
#     avg_b = np.average(result[:, :, 2])
#     for x in range(result.shape[0]):
#         for y in range(result.shape[1]):
#             l, a, b = result[x, y, :]
#             l *= 100 / 255.0
#             result[x, y, 1] = a - ((avg_a - 128) * (l / 100.0) * 1.1)
#             result[x, y, 2] = b - ((avg_b - 128) * (l / 100.0) * 1.1)
#     result = cv2.cvtColor(result, cv2.COLOR_LAB2BGR)
#     return result

# final = np.hstack((img, white_balance_loops(img)))
# show(final)
# cv2.imwrite('result.jpg', final)
# # cv2.imshow('new', eyeimg(img))
# cv2.waitKey(0)





