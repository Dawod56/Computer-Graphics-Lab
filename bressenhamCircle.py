import cv2
import numpy as np


image =np.zeros((600,800,3),np.uint8)
image.fill(255)
r=100



def midpointCircle(x,y,r):

    points=[]
    x1 = 0
    y1 = r
    d =  1- r
    while (x1 <= y1):
        points.append((x1 + x, y1 + y))
        points.append((y1 + x, x1 + y))
        points.append((y1 + x, -x1 + y))
        points.append((x1 + x, -y1 + y))
        points.append((-x1 + x, -y1 + y))
        points.append((-y1 + x, -x1 + y))
        points.append((-y1 + x, x1 + y))
        points.append((-x1 + x, y1 + y))

        x1 = x1 + 1

        if d < 0:
            d = d + 2 * x1 + 3
        else:
            d = d + 2 * x1 - 2 * y1 + 5
            y1 = y1 - 1

    return points


def bressenhamCircle(x,y,r):
    points=[]
    x1=0
    y1=r
    d=3-2*r
    while(x1<=y1):
        points.append((x1+x,y1+y))
        points.append((y1+x, x1+y))
        points.append((y1+x, -x1+y))
        points.append((x1+x, -y1+y))
        points.append((-x1+x, -y1+y))
        points.append((-y1+x, -x1+y))
        points.append((-y1+x, x1+y))
        points.append((-x1+x, y1+y))

        x1=x1+1

        if d<0:
            d=d+4*x1+6
        else:
            d=d+4*x1-4*y1+10
            y1=y1-1

    return points




def clickEvent(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        g=x
        h=y

        list=bressenhamCircle(g,h,r)
        list2=midpointCircle(g,h,r)



        j = len(list)
        k=len(list2)
        for l in range(j):
            cv2.circle(image, list[l], 2, (255, 255, 0), -1)
            # cv2.circle(image, list2[l], 0, (255, 0, 0), -1)

            cv2.imshow('Draw', image)

        for l in range(k):
            cv2.circle(image, list[l], 1, (0, 0, 255), -1)
            # cv2.circle(image, list2[l], 0, (255, 0, 0), -1)

            cv2.imshow('Draw', image)


cv2.imshow('Draw', image)
cv2.setMouseCallback('Draw', clickEvent)
cv2.waitKey(0)
cv2.destroyAllWindows()