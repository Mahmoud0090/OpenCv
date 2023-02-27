import cv2 as cv

def rescaleFrame(frame , scaleSize = 0.75):
    # images , vidoes and live videos
    width = int(frame.shape[1] * scaleSize)
    height = int(frame.shape[0] * scaleSize)

    dim = (width , height)

    return cv.resize(frame , dim , interpolation = cv.INTER_AREA)


def changeRes(width , height):
    # live video only
    capture.set(3 , width)
    capture.set(4 , height)

#reading and resizing image
img = cv.imread("photos\covid.jpg")
resized_img = rescaleFrame(img)

cv.imshow("img",img)
cv.imshow("resizedImg",resized_img)


#reading video and resizing it

capture = cv.VideoCapture("videos/game.mp4")

while True:
    Istrue , frame = capture.read()
    resizedFrame = rescaleFrame(frame)

    cv.imshow("video" , frame)
    cv.imshow("resizedVideo" , resizedFrame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

