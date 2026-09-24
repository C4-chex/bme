enumerate(可迭代对象, start=0[start=任意数])

eg:
    a = ['apple', 'banana', 'cherry']

        for i, item in enumerate(a):
            print(i, item)

应用范围包括：
    dict 
        d = {'a': 1, 'b': 2, 'c': 3}

        for i, key in enumerate(d):
            print(i, key)

    str
        for i, ch in enumerate("abc"):
            print(i, ch)