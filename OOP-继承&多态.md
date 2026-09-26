


class M:
    def __init__(self,name,sex):
        self.name = name
        self.sex = sex
        self.eye = 2

    def breathe(self):
        print(self.name + 'breathing')

    def poop(self):
        print(self.name + 'pooping')

class Human(M):                         #这个部分 Human不是作为M的内部类 不用缩进
    def __init__(self,name,sex):        #这里 此行用于按照父class初始化子class 要不然无法def子class的特有属性
        super().__init__(name,sex)      #super用于明确在初始化后所引用的部分 
        self.has_tail = True

h = Human ('s','1')             #创建实例
print(h.has_tail)               #注意 此处如果想print所有属性的话 可以写 print(h.__dict__)