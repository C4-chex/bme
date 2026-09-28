#对于isinstance
#isinstance 返回的是bool值
#isinstance(对象，类或者类型）
print(isinstance(10,int)) #判断单个类型

#但是
print(isinstance(10,(int,float)))
#也可以在后部分传入一个元组 只要满足其一就会返回Ture

#或者判断一个实例是不是在某个class中
class f:
        pass

class g(f):
    pass

chex = g()
print(isinstance(chex,f)) #这里演示了isinstance的继承性质

print(type(chex) == f)   #type就不具有继承性质
