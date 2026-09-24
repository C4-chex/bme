Decimal 的运算受上下文控制，默认精度是 28 位有效数字。可以通过 getcontext() 修改：
    from decimal import Decimal, getcontext

    getcontext().prec = 5   # 设置精度为 5 位有效数字

    print(Decimal('1') / Decimal('3'))   # 0.33333



decimal 提供了多种舍入方式，通过 getcontext().rounding 设置，或直接在 quantize() 中指定：
    from decimal import Decimal, ROUND_HALF_UP, ROUND_DOWN, ROUND_CEILING

    d = Decimal('2.675')

    print(d.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))   # 2.68
    print(d.quantize(Decimal('0.01'), rounding=ROUND_DOWN))      # 2.67
    print(d.quantize(Decimal('0.01'), rounding=ROUND_CEILING))   # 2.68
    
    ROUND_HALF_UP	四舍五入    ROUND_CEILING	向正无穷舍入      ROUND_DOWN	向零截断

f'式格式化输出

    d = Decimal('3.14159')
    print(f"{d:.2f}")   # 3.14 不过因为先转化为folat再向decimal转化会有精度差距
  故优先选用

    print(d.quantize(Decimal('0.01')))   # 3.14