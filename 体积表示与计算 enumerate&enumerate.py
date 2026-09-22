
from decimal import Decimal

a = [55.6126, 5.7422, 44.3901, 48.8239, 67.3939, 1.5930, 8.6702, 6.2483, 62.9102, 25.8639]

for x in a:
    y = Decimal(str(x)) * 10   #对于精确数据的倍化处理
    if y > 100:            #注意 这个地方不可直接引用float 如：decimal（0.1）
        print(y)                              #会报错 要写成str形式（"0.1")
#   print(sum(Decimal(str(a))))  ————这样写会报错 因为decimal无法转化str
total = sum(Decimal(str(x)) for x in a)
print('total:',total)

for i, volume in enumerate(a, start=1):
    print("第", i, "个病例：", volume)
