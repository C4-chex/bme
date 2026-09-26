class Chex:
    def __init__(self,brand:str,power:str) -> None:
        self.brand = brand
        self.power = power
        self.turn: bool = False



    def turn_on(self)->None:
        if self.turn:
            print('1')
        else :
            self.turn = True
            print('0')

smeg=Chex('dw','da')
#上
smeg.turn_on()
print('w')

                                        #上下是两中不同的调用方法 上：使用smeg代指Chex 下在.turn_on()中调用
                                        #我也不知道有啥区别 反正感觉前面好用点
                                        #总之 别Chex.turn_on 就行
#下
Chex.turn_on(smeg)
print('m')