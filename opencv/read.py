import cv2 as cv

# reading image
# img = cv.imread("photos\covid.jpg")
#
# cv.imshow("n" , img)
#
# cv.waitKey(0)

#reading video

capture = cv.VideoCapture("videos/game.mp4")

while True:
    Istrue , frame = capture.read()
    cv.imshow("video" , frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()



