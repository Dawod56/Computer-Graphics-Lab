import cv2
import numpy as np


image =np.zeros((600,800,3),np.uint8)
image.fill(255)

xp=[]
yp=[]

def bressenhamLine(x1,y1,x2,y2):

    points=[]
    x=x1
    y=y1
    dx=x2-x1
    dy=y2-y1

    points.append((int(x), int(y)))


    if abs(dx)>abs(dy):
        p0=2*abs(dx)-abs(dy)
        xinc=int(dx/abs(dx))
        yinc=int(dy/abs(dy))


        for i in range(abs(dx)+1):

            x=x+xinc

            if p0<0:
                p0=p0+2*abs(dy)
            else:
                p0=p0+2*abs(dy)-2*abs(dx)
                y=y+yinc
            points.append((x, y))


    else:
        xinc = dx / abs(dx)
        yinc = dy / abs(dy)
        p0 = 2 * abs(dy) - abs(dx)

        for i in range(abs(dy)+1):

            y = y + yinc

            if p0 < 0:
                p0 = p0 + 2 * abs(dx)
            else:
                p0 = p0 + 2 * abs(dx) - 2 * abs(dy)
                x = x + xinc
            points.append((int(x), int(y)))

    return points







def clickEvent(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        xp.append(x)
        yp.append(y)


        if len(xp)>=2:
            a=xp[-2]
            b=yp[-2]
            c=xp[-1]
            d=yp[-1]
            list= bressenhamLine(a,b,c,d)
            #list2 = line(a, b, c, d)
            j = len(list)

            for l in range(j):

                cv2.circle(image, list[l], 1, (0, 255, 195), -1)
                #cv2.circle(image, list2[l], 0, (255, 0, 0), -1)

                cv2.imshow('Draw', image)






cv2.imshow('Draw', image)
cv2.setMouseCallback('Draw', clickEvent)
cv2.waitKey(0)
cv2.destroyAllWindows()
