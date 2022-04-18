import matplotlib.pyplot as plt

plt.title("Mid Point ellipse Drawing ")
plt.xlabel("X axis")
plt.ylabel("Y axis")
A = float(input("Enter the major axis:"))
B = float(input("Enter the minor axis:"))

x1=0
x2=0
y1=0
y2=0
x1coordinates = []
x2coordinates = []
y1coordinates = []
y2coordinates = []

x = 0;
y = B;

p1 = ((B * B) - (A * A * B) + (0.25 * A * A));
dx = 2 * B * B * x;
dy = 2 * A * A * y;


while (dx < dy):

    x1 = x
    x2 = (-1) * x
    y1 = y
    y2 = (-1) * y

    x1coordinates.append(x1)
    x2coordinates.append(x2)
    y1coordinates.append(y1)
    y2coordinates.append(y2)

    if (p1 < 0):
        x += 1;
        dx = dx + (2 * B * B);
        p1 = p1 + dx + (B * B);
    else:
        x += 1;
        y -= 1;
        dx = dx + (2 * B * B);
        dy = dy - (2 * A * A);
        p1 = p1 + dx - dy + (B * B);

p2 = (((B * B) * ((x + 0.5) * (x + 0.5))) + ((A * A) * ((y - 1) * (y - 1))) - (A * A * B * B));

while (y >= 0):

    x1 = x
    x2 = (-1) * x
    y1 = y
    y2 = (-1) * y

    x1coordinates.append(x1)
    x2coordinates.append(x2)
    y1coordinates.append(y1)
    y2coordinates.append(y2)


    if (p2 > 0):
        y -= 1;
        dy = dy - (2 * A * A);
        p2 = p2 + (A * A) - dy;
    else:
        y -= 1;
        x += 1;
        dx = dx + (2 * B * B);
        dy = dy - (2 * A * A);
        p2 = p2 + dx - dy + (A * A);








plt.plot(x1coordinates, y1coordinates)
plt.plot(x1coordinates, y2coordinates)
plt.plot(x2coordinates, y1coordinates)
plt.plot(x2coordinates, y2coordinates)


plt.show()
