import cv2 as cv

img = cv.imread('photos/cat.jpg')
img = cv.resize(img , (500,500))
cv.imshow('img', img)


gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('gray' , gray)

#simple threshold
threshold , thresh = cv.threshold(gray , 150 , 255 , cv.THRESH_BINARY)
cv.imshow('thresh' , thresh)
print(threshold) # will print 150

threshold , thresh_inv = cv.threshold(gray , 150 , 255 , cv.THRESH_BINARY_INV)
cv.imshow('thresh inverse' , thresh_inv)

#adaptive threshold
adaptive_thresh = cv.adaptiveThreshold(gray , 255 , cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11 ,3)
cv.imshow('adaptive thresh' , adaptive_thresh)

cv.waitKey(0)