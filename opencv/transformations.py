import cv2 as cv
import numpy as np

img = cv.imread("photos/cat.jpg")

img = cv.resize(img , (500,500))

cv.imshow("img" , img)

#translations

def translations(img , x , y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dim = (img.shape[1] , img.shape[0])
    return cv.warpAffine(img , transMat, dim)

# -x -> left
# x ->  right
# -y -> up
# y -> down

translated = translations(img , 100 ,-100)
cv.imshow("translated" , translated)


#rotation

def rotation(img , angle , rotPoint = None):
    (width,height) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2 , height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint , angle , 1.0)
    dim = (width , height)

    return cv.warpAffine(img , rotMat , dim)

rotated = rotation(img , -45)
cv.imshow("rotated" , rotated)

#flipping

flipped = cv.flip(img , 0) # 0 for vertical flipping  and 1 for horizontal flipping
cv.imshow("flipped" , flipped)

cv.waitKey(0)