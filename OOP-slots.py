#对于OOP还有一些较进阶内容
#1- __slots__


class f:
    def __init__(self,name,age)->None:
        pass                    #这个是一般的def方法    不限制实例的属性添加







class g(object):
    __slots__ = ('sex','score')         #限制
anle = g()                              #但是在这里注意 __slots__只限制实例 不限制类
anle.sex = 'boy'                        #这意味着：其实是可以在后期对class添加属性的
print(anle.sex)

class h(g):                             #在继承中  子class是继承了父class的属性内容的
    pass                                #这意味着 子class如果不写 __slots__ 其实就是一个dict
o = h()                                 #写了slots的话就是子class的slots加上父class的slots
o.sex = 'girl'
print(o.sex)