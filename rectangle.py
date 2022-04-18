import cv2
import numpy as np


image =np.zeros((600,800,3),np.uint8)
image.fill(255)
a=120
b=80

def rectangle(x, y, a, b):
    points = []
    for i in range(a):
        points.append((x + i, y))
        points.append((x + i, y-b))

    for i in range(b):
        points.append((x, y-i))
        points.append((x + a, y-i))


    return points








def clickEvent(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        g=x
        h=y

        list=rectangle(g,h,a,b)

        j = len(list)
        for l in range(j):
            cv2.circle(image, list[l], 1, (0, 255, 255), -1)


            cv2.imshow('Draw', image)






cv2.imshow('Draw', image)
cv2.setMouseCallback('Draw', clickEvent)
cv2.waitKey(0)
cv2.destroyAllWindows()