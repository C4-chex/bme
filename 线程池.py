import time
import threading
from concurrent.futures import ThreadPoolExecutor

lock = threading.Lock()

def f(x):
    with lock :      #锁住start和对应的x 保证两者对其
        print('start',x)
    time.sleep(0.1)

pool = ThreadPoolExecutor(10)     #创建线程池
web = ["www.xxx{}".format(i) for i in range(100)]   #tip：{}作为占位格收取.format的range参数


for i in web:
    pool.submit(f,i)
#submit的用法：submit（函数id，*args，*kwargs）
#这里因为f函数有参数 所以必须在submit后面补参数

print('developing')

pool.shutdown(True) #shutdown 用于等待线程池中所有任务完成后在继续执行主程序
print('done')