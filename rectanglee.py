import matplotlib.pyplot as plt

plt.title("R E C T A N G L E")
plt.xlabel("X axis")
plt.ylabel("Y axis")

x1c=[]
x2c=[]
y1c=[]
y2c=[]

x1 = int(input("x1:"))
y1 = int(input("y1:"))
a = int(input("Length A:"))
b = int(input("Width B:"))

for i in range(a):
    x1c.append((x1 + i))
    y1c.append(y1)



for i in range(b):
    y1c.append(y1+i)
    y2c.append(y1+a-i)

plt.plot(x1c,y1c)



plt.show()