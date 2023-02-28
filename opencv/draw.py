import cv2 as cv
import numpy as np

# making blank image
blank = np.zeros((500,500,3) , dtype = 'uint8')
cv.imshow("blank" , blank)

# make the image green
#blank[:] = 0,255,0

#cv.imshow("green" , blank)

# colouring small portion of the image
#blank[200:300 , 300:400] = 0,0,155  # the portion is red

#cv.imshow("portion" , blank)

#draw a rectangle

cv.rectangle(blank , (0,0), (blank.shape[1]//2 , blank.shape[0]//2) , (0,255,0),thickness = -1) #thickness -1 will fill with color

cv.imshow("rect" , blank)

#draw a circle
cv.circle(blank , (blank.shape[1]//2 , blank.shape[0]//2) , 40 , (0,0,255),thickness = -1)
cv.imshow("cir" , blank)

#draw a line
cv.line(blank , (0,0) , (blank.shape[1]//2 , blank.shape[0]//2) , (255,0,0) , thickness = 2)
cv.imshow("line" , blank)

# write a text
cv.putText(blank , "Hello" , (0,225) , cv.FONT_HERSHEY_TRIPLEX , 1.0 ,(255,255,255) , 2)
cv.imshow("text" , blank)

# the image will not close until we hit the close button
cv.waitKey(0)