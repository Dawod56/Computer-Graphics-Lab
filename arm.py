import math

import cv2
import numpy as np



image =np.zeros((600,800,3),np.uint8)
image.fill(255)


def printline(param, list,r,g,b):
    j=len(list)
    for l in range(j):
        u = list[l]
        cv2.circle(image, (math.floor(u[0]),math.floor(u[1])), 2, (b, g, r), 5)
        cv2.imshow(param, image)
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
        points.append((p,q))
        p = p + xinc
        q = q + yinc

    return points
def shiftLine(l1, tx, ty):
    points=[]
    l=len(l1)
    for i in range(l):
        u=l1[(i)]
        x=u[0]
        y=u[1]
        x1=x+tx
        y1=y+ty
        points.append((x1,y1))


    return points
def rotateCenter(l1, param):
    points = []
    a = (param * math.pi) / 180
    sin = math.sin(a)
    cos = math.cos(a)

    l = len(l1)
    for i in range(l):
        u = l1[(i)]
        x = u[0]
        y = u[1]
        x1 = x*cos-y*sin
        y1 = x*sin+y*cos
        points.append((x1,y1))

    return points
def rotateLine(l1, param):

    u=l1[0]
    tx=0-u[0]
    ty=0-u[1]
    l1=shiftLine(l1,tx,ty)
    l1=rotateCenter(l1,param)
    l1=shiftLine(l1,-tx,-ty)
    return l1



def draw():
    printline('Draw', l1, 255, 0, 0)
    printline('Draw', l2, 0, 255, 0)
    printline('Draw', l3, 0, 0, 255)




l1=ddr_line(225,343,318,231)
l2=ddr_line(318,231,261,175)
l3=ddr_line(261,175,243,216)
printline('Draw',l1,255,0,0)
printline('Draw',l2,0,255,0)
printline('Draw',l3,0,0,255)


#cv2.setMouseCallback('Draw', clickEvent)

while True:
    cv2.imshow('Draw', image)
    k = cv2.waitKey(1)
    if (k == ord('s')):
        tx = int(input("Enter tx: "))
        ty = int(input("Enter ty: "))
        l1 = shiftLine(l1, tx, ty)
        l2 = shiftLine(l2, tx, ty)
        l3 = shiftLine(l3, tx, ty)
        image = np.zeros((600, 800, 3), np.uint8)
        image.fill(255)
        draw()


    if(k==ord('b')):
        a=int(input("Enter angle: "))
        l3=rotateLine(l3,a)
        image = np.zeros((600, 800, 3), np.uint8)
        image.fill(255)
        draw()

    if(k==ord('g')):
        a=int(input("Enter angle: "))
        l2=rotateLine(l2,a)

        u=l2[-1]
        v=l3[0]
        tx=u[0]-v[0]
        ty=u[1]-v[1]
        l3=shiftLine(l3,tx,ty)
        l3 = rotateLine(l3, a)
        image = np.zeros((600, 800, 3), np.uint8)
        image.fill(255)
        draw()

    if (k == ord('r')):
        a = int(input("Enter angle: "))
        l1 = rotateLine(l1, a)

        u = l1[-1]
        v = l2[0]
        tx = u[0] - v[0]
        ty = u[1] - v[1]
        l2 = shiftLine(l2, tx, ty)
        l2 = rotateLine(l2, a)
        u = l2[-1]
        v = l3[0]
        tx = u[0] - v[0]
        ty = u[1] - v[1]
        l3 = shiftLine(l3, tx, ty)
        l3 = rotateLine(l3, a)
        image = np.zeros((600, 800, 3), np.uint8)
        image.fill(255)
        draw()



    if(k==27):
        cv2.destroyAllWindows()
        break

