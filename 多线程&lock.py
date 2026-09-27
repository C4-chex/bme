import threading



num = 0
lock = threading.Lock()            #创建安全锁 注意 f&f2应该使用同一安全锁 否则依旧是os系统自动随机分片运行
def f():
    lock.acquire()                  #加锁
    global num                      #因为函数内部要引用全局变量num 所以使用global 变量名 来引入
    for i in range(100):
        num += 1
        print(num)
    lock.release()                  #解锁

def f2():
    lock.acquire()
    global num
    for i in range(10):
        num -=1
        print(num)
    lock.release()


def f3():                                       #with lock支持上下文用法
    global num                                  #这样写比手动lock & release更加简单和安全
    for i in range(10):
        with lock:
            num +=1
            print(num)

#进程
t1 = threading.Thread(target=f)
t2 = threading.Thread(target=f2)
t3 = threading.Thread(target=f3)
t1.start()
t3.start()
t2.start()
t2.join()
t1.join()
t3.join()
print(num)

