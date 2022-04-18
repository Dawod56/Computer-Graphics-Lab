import cv2
import numpy as np


image =np.zeros((600,800,3),np.uint8)
image.fill(255)
a=90
b=40

def midpointElipse(g,h,a,b):
    points=[]
    x=0
    y=b
    p1=b*b-a*a*b+(.25*a*a)
    dx=2*b*b*x
    dy=2*a*a*y
    while(dx<dy):
        points.append((x+g,y+h))
        points.append((-x + g, y + h))
        points.append((-x + g, -y + h))
        points.append((x + g, -y + h))
        x=x+1
        dx=dx+2*b*b
        if(p1<0):
            p1=p1+dx+2*b*b
        else:
            y=y-1
            dy=dy-2*a*a
            p1=p1+dx+b*b-dy


    p2=b*b*x*x+a*a*y*y-a*a*b*b

    while(y>=0):
        points.append((x + g, y + h))
        points.append((-x + g, y + h))
        points.append((-x + g, -y + h))
        points.append((x + g, -y + h))
        y = y - 1
        dy = dy - 2 * a * a

        if(p2>0):
            p2=p2-dy+a*a

        else:
            x=x+1
            dx=dx+2*b*b
            p2=p2+dx-dy+a*a



    return points




def clickEvent(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        g=x
        h=y

        list=midpointElipse(g,h,a,b)

        j = len(list)
        for l in range(j):
            cv2.circle(image, list[l], 1, (0, 255, 0), -1)


            cv2.imshow('Draw', image)






cv2.imshow('Draw', image)
cv2.setMouseCallback('Draw', clickEvent)
cv2.waitKey(0)
cv2.destroyAllWindows()