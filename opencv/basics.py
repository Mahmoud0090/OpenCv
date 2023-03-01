import cv2 as cv

img = cv.imread("photos/cat.jpg")

def rescaleFrame(frame , scaleSize = 0.75):
    # images , vidoes and live videos
    width = int(frame.shape[1] * scaleSize)
    height = int(frame.shape[0] * scaleSize)

    dim = (width , height)

    return cv.resize(frame , dim , interpolation = cv.INTER_AREA)

img = rescaleFrame(img , scaleSize=0.25)

cv.imshow("cat" , img)

#convert to grayscale

gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)

#cv.imshow("gray" , gray)

# BLur
blur = cv.GaussianBlur(img , (9,9) , cv.BORDER_DEFAULT) # to increase the blur we increase (3,3) to a higher ODD num
#cv.imshow("Blur" , blur)

#Edge cascade (showing edges in image)

canny = cv.Canny(img , 125 , 175)
#cv.imshow('canny' , canny)

#the edges can be reduced by passing the blur image
blurcanny = cv.Canny(blur , 125, 175)
#cv.imshow('blurcanny' , blurcanny)

#dilating the image: make the edges of canny image thicker
dilated = cv.dilate(canny , (7,7) , iterations =3)
#cv.imshow('dilated' , dilated)

#eroding the image : make the edges thinner almost convert above dilated to canny again
eroded = cv.erode(dilated , (7,7) , iterations =5)
#cv.imshow('eroded' , eroded)

#Resize

resized = cv.resize(img , (500,500))
cv.imshow('resized', resized)

#Cropping

cropped = img[50:200 , 200:400]
cv.imshow('cropped' , cropped)

cv.waitKey(0)