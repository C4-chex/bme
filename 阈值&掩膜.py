import matplotlib.pyplot as plt
a = [
    [1,2,3,4,5],
    [8,9,10,11,12],
    [13,14,15,16,17],
    [1,54,36,74,84],
    [12,45,35,63,73],
]
c=[]
vmax=1
vmin=0
for row in a:
    b=[]
    for col in row:
        if col>int(5):
            b.append(1)
        else:
            b.append(0)
    c.append(b)

for x in c:
    print(x)
plt.figure()
plt.imshow(c,cmap='gray')
plt.show()
