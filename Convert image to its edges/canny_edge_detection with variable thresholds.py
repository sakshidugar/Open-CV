# import numpy as np
import cv2 as cv

def nothing(a):
    pass


cv.namedWindow("window")
cv.createTrackbar("Threshold1", "window", 0, 300, nothing)
cv.createTrackbar("Threshold2", "window", 0, 300, nothing)


while True:
    # thresh1=100
    # thresh2=200
    image = cv.imread("/home/sakshi108/Downloads/snap.jpg")
    image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    thresh1 = cv.getTrackbarPos("Threshold1", "window")
    thresh2 = cv.getTrackbarPos("Threshold2", "window")
    img1 = cv.Canny(image, thresh1, thresh2)
    cv.imshow("image",image)
    cv.imshow("image1",img1)
    if cv.waitKey(5) & 0xff==ord('q'):
        break