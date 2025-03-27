#进程
# python中的多线程其实并不是真正的多线程，如果想要充分使用多核CPU的资源，在python中大部分情况需要使用
# 多进程
# python提供了multiprocessing，只需要定义一个函数，python会完成其他所有事情。
# 可以轻松完成单进程到并发执行的转化。multiprocessing支持子进程/通信和共享数据/执行不同形式的同步
# 提供了Process,Queue,Pipe,Lock


import multiprocessing
import time

# def worker(interval,name):
#     print(name + '[start]')
#     time.sleep(interval)
#     print(name + '[end]')

# if __name__ == '__main__':
#     p1 = multiprocessing.Process(target=worker,args=(2,'huohuazi1016'))
#     p2 = multiprocessing.Process(target=worker,args=(222,'huohuazi1016'))
#     p3 = multiprocessing.Process(target=worker,args=(222,'huohuazi1016'))

#     p1.start()
#     p2.start()
#     p3.start()

#     print("the number of CPU is:" + str(multiprocessing.cpu_count()))
#     for p in multiprocessing.active_children():
#         print("child p.name:" + p.name + '\tp.id' + str(p.pid))
#     print("END")

# class ClockProcess(multiprocessing.Process):
#     def __init__(self,interval):
#         multiprocessing.Process.__init__(self)
#         self.interval = interval

#     def run(self):
#         n = 5
#         while n > 0:
#             print("time: {0}".format(time.ctime()))
#             time.sleep(self.interval)
#             n -=1

# if __name__ == '__main__':
#     p=ClockProcess(5)
#     p.start()

# daemon属性
    #没有加daemon属性
# def worker(interval):
#     print('start time:{0}'.format(time.ctime()))
#     time.sleep(interval)
#     print('start end:{}'.format(time.ctime()))

# if __name__ == '__main__':
#     p = multiprocessing.Process(target=worker,args=(3,))
#     p.start()
#     print('end')