import threading

class MyThread(threading.Thread):               #用class来让MyThread继承threading.Thread
    def run(self):              #run里面写该线程要执行的代码
        print('执行此线程',self._args)


t1 = MyThread(args=(100,))
t1.start()