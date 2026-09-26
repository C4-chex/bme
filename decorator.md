对于一个装饰器 基本用法：
    def a#语法糖名（func#即被调用的函数的代称）：
        def x#普通函数：
            #这个部分写在原函数执行前触发的程序
            func（）  #注意这个部分事关原函数的参数问题---------------------------
            #这个部分写在原函数执行后触发的程序                                  |
        return x  #这里用x做代存 返回给a()                                    |
                                                                           |
然后在需要被装饰的函数前一行引用decorator：                                      |
    @a                                                                     |
    即可                                                                    |
                                                                           |
    因为如果原函数带参数而func的括号内不带的话会报错                           <----
    所有一般选择使用func（*args,**kwargs)传参


def decorator(func):
    def x(*args, **kwargs):
        val = func(*args, **kwargs)
        return val
    return x

@decorator
def plus(x, y):
    print(x + y)
    return ('算完了')
print(plus(1, 2))


比如在这个程序中
    如果原函数已经有了return的定数 那么如果不把func（...）赋值 则会因为func的值未被接收导致报错