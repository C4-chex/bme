import multiprocessing

def f():
    pass

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=f)
    p1.start()