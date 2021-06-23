import cv2 as cv

# #### suppose coordinates of copied image is (x1copy,y1copy) and (x2copy,y2copy)
# #### and coordinates of region to be paste is (x1paste,y1paste) and (x2paste,y2paste)
#  then (y2copy-y1copy)==(y2paste-y1paste) and (x2copy-x1copy)==(x2paste-x1paste)
#  need to be taken care
# for that we took diff1 for y-coordinates and diff2 for x-coordinates and compensated it.

def click_coordinates(event,x,y,flags,param):
    if event==cv.EVENT_LBUTTONDOWN:
        points.append((x,y))
        if(len(points)==4):
            x1copy,y1copy=points[-4][0],points[-4][1]   #  y1copy=points[-4][1]
            x2copy,y2copy=points[-3][0],points[-3][1]   # y2copy=points[-3][1]
            x1paste,y1paste=points[-2][0],points[-2][1]     # y1paste=points[-2][1]
            x2paste,y2paste = points[-1][0],points[-1][1]   # y2paste = points[-1][1]

            diff1=(y2copy-y1copy)-(y2paste-y1paste)
            diff2=(x2copy-x1copy)-(x2paste-x1paste)
            # ball=img[x1copy:y1copy,x2copy:y2copy]
            # img[x1paste:y1paste,x2paste:y2paste]=ball
            ball = img[y1copy:y2copy, x1copy:x2copy]
            img[y1paste:y2paste+diff1, x1paste:x2paste+diff2] = ball
            value=[i for i in points]
            print(value)
            points.clear()


points=[]
img=cv.imread("toys.jpeg")
cv.imshow("window",img)
cv.setMouseCallback("window",click_coordinates)
while(1):
    cv.imshow("window",img)
    if cv.waitKey(1) & 0Xff==ord('q'):
        break
