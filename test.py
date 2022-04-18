import matplotlib.pyplot as plt

x0 = int(input())
y0 = int(input())
x1 = int(input())
y1 = int(input())

M = (y1-y0)/(x1-x0)

if 0 < M < 1:
    a = x0
    b = y0
    x = []
    y = []
    while b < y1 and a < x1:
        x.append(a)
        y.append(y)
        print("X1: ", x1, "Y1: ", y1)
        a = a+1
        b = b+M

    plt.plot(x, y)
    plt.grid()
    plt.show()

elif -1 < M <= 0:
    a = x0
    b = y0
    x = []
    y = []
    while b < y1 and a < x1:
        x.append(a)
        y.append(y)
        print("X1: ", x1, "Y1: ", y1)
        a = a - 1
        b = b - M

    plt.plot(x, y)
    plt.grid()
    plt.show()

elif M > 1:
    a = x0
    b = y0
    x = []
    y = []
    while b < y1 and a < x1:
        x.append(a)
        y.append(y)
        print("X1: ", x1, "Y1: ", y1)
        a = a + (1/M)
        b = b +1

    plt.plot(x, y)
    plt.grid()
    plt.show()

else:

    a = x0
    b = y0
    x = []
    y = []
    while b < y1 and a < x1:
        x.append(a)
        y.append(y)
        print("X1: ", x1, "Y1: ", y1)
        a = a - (1/M)
        b = b - 1

    plt.plot(x, y)
    plt.grid()
    plt.show()
