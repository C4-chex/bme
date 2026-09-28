class Student(object):
    @property
    def score(self):
        return self._score          #一个约定俗成的写法 即_变量名 意味着该变量是内部变量 非必要别动

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    @property
    def ping(self):
        return self._score


#test
tom = Student()
tom.score = 10
print(tom.score)
tom.score = 20
print(tom.score)
print(tom.ping)
tom.ping = 30




