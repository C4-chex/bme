def decorator(func):
    def x(*args, **kwargs):
        val = func(*args, **kwargs)
        return val
    return x

@decorator
def plus(x, y):
    print(x + y)
    return '算完了'
print(plus(1, 2))
