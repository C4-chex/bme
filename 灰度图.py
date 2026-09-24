import matplotlib.pyplot as plt

a = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

# 图1：默认范围
plt.figure()
plt.imshow(a, cmap='gray')
plt.show()

