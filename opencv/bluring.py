import cv2 as cv

img = cv.imread('photos/cat.jpg')
img = cv.resize(img , (500,500))

cv.imshow('img' , img)

#averaging
average = cv.blur(img,(7,7)) # 7,7 is the filter size
cv.imshow('avg' , average)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian Blur', gauss)

# Median Blur
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# Bilateral
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)