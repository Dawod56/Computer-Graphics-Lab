import math

import cv2
import numpy as np


image =np.zeros((600,800,3),np.uint8)
image.fill(255)

xp=[]
yp=[]

def ddr_line(x1,y1,x2,y2):
    points = []
    dx = x2 - x1
    dy = y2 - y1
    if abs(dx) >= abs(dy):
        step = abs(dx)
    else:
        step = abs(dy)

    xinc = dx / step
    yinc = dy / step

    p = x1
    q = y1



    for i in range(step):
        points.append((math.floor(p),math.floor(q)))
        p = p + xinc
        q = q + yinc

    return points


def line(x1,y1,x2,y2):
    #flag = 0
    points2=[]

    dx = x2 - x1
    dy = y2 - y1

    m = dy / dx
    c = y1 - m * x1
    #c1 = c / m

    if abs(dx) >= abs(dy):
        step=abs(dx)
        incx = dx/abs(dx)

    else:
        step = abs(dy)
        incx=dx/abs(dy)
       # flag = 1


    r = x1
    s = y1
    #if flag == 0:
    for i in range(step):

            points2.append((math.floor(r),math.floor(s)))
            r = r + incx
            s = m * r + c

    #elif flag == 1:
        #for i in range(step):
            #points2.append((math.floor(r),math.floor(s)))
            #s = s + incy
            #r = (s + c)/m

    return points2


def clickEvent(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        xp.append(x)
        yp.append(y)


        if len(xp)>=2:
            a=xp[-2]
            b=yp[-2]
            c=xp[-1]
            d=yp[-1]
            list= ddr_line(a,b,c,d)
            list2 = line(a, b, c, d)
            j = len(list)

            for l in range(j):
                cv2.circle(image, list[l], 1, (0, 0, 255), -1)
                cv2.circle(image, list2[l], 0, (255, 0, 0), -1)

                cv2.imshow('Draw', image)






cv2.imshow('Draw', image)
cv2.setMouseCallback('Draw', clickEvent)
cv2.waitKey(0)
cv2.destroyAllWindows()

