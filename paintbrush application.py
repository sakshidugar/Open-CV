import cv2 as cv
import numpy as np

drawing = False # true if mouse is pressed


def nothing(a):
    pass

# mouse callback function
def draw_circle(event,x,y,flags,param):
    global drawing
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
    if event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
             cv.circle(img,(x,y),5,(b,g,r),-1)
    elif event == cv.EVENT_LBUTTONUP:
         drawing = False


img = np.ones((512,512,3), np.uint8)
img1= np.ones((512,512,3), np.uint8)
cv.namedWindow("window")

# create color tracker
cv.createTrackbar("R","window",0,255,nothing)
cv.createTrackbar("G","window",0,255,nothing)
cv.createTrackbar("B","window",0,255,nothing)

cv.namedWindow('image')
cv.setMouseCallback('image',draw_circle)
while(1):

    # color selection for painting
    r = cv.getTrackbarPos("R", "window")
    g = cv.getTrackbarPos("G", "window")
    b = cv.getTrackbarPos("B", "window")
    print(r, g, b)
    # shows the color chosen using colortracker
    img1[:] = [b, g, r]
    cv.imshow('image',img)
    cv.imshow("window", img1)
    # press q to exit from program
    if cv.waitKey(1) & 0xFF==ord('q'):
        break

cv.destroyAllWindows()