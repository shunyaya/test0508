import cv2
import numpy as np
# contrast stretching

# read image
img = cv2.imread('media\\yayaseye.jpg', cv2.IMREAD_COLOR)

# normalize float versions
norm_img1 = cv2.normalize(img, None, alpha=0, beta=1,
                          norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
norm_img2 = cv2.normalize(img, None, alpha=0, beta=1.2,
                          norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)

# scale to uint8
norm_img1 = (255*norm_img1).astype(np.uint8)
norm_img2 = np.clip(norm_img2, 0, 1)
norm_img2 = (255*norm_img2).astype(np.uint8)

# write normalized output images
cv2.imwrite("zelda1_bm20_cm20_normalize1.jpg", norm_img1)
cv2.imwrite("zelda1_bm20_cm20_normalize2.jpg", norm_img2)

# display input and both output images
cv2.imshow('original', img)
cv2.imshow('normalized1', norm_img1)
cv2.imshow('normalized2', norm_img2)
cv2.waitKey(0)
cv2.destroyAllWindows()




# img = cv2.imread('media\\eye.jpg')
# original = img.copy()
# xp = [0, 64, 128, 192, 255]
# fp = [0, 16, 128, 240, 255]
# x = np.arange(256)
# table = np.interp(x, xp, fp).astype('uint8')
# img = cv2.LUT(img, table)
# cv2.imshow("original", original)
# cv2.imshow("Output", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
