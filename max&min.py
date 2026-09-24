from decimal import Decimal, getcontext, ROUND_CEILING
result = {}
v = [5.5084, 10.5156, 6.3956, 7.7872, 7.5946,
     9.1309, 6.5231, 5.9775, 8.4490, 14.8868]

pi = Decimal('3.14')   # 更精确可用 Decimal('3.14159265358979323846')

def fx(x):
    return Decimal('4') * pi * x ** 3 / Decimal('3')

for idx,i in enumerate(v, start=1):
    x = Decimal(str(i))   # 关键：转成 Decimal
    R = fx(x)
    r=R.quantize(Decimal('0.0001'), rounding=ROUND_CEILING)
    result[idx]=r

print(result)
max_value = max(result.items(),key=lambda x: x[1])
min_value = min(result.items(),key=lambda x: x[1])
print(max_value)
print(min_value)
