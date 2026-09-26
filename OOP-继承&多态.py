


class M:
    def __init__(self,name,sex):
        self.name = name
        self.sex = sex
        self.eye = 2

    def breathe(self):
        print(self.name + 'breathing')

    def poop(self):
        print(self.name + 'pooping')

class Human(M):
    def __init__(self,name,sex):
        super().__init__(name,sex)
        self.has_tail = True

h = Human ('s','1')
print(h.has_tail)