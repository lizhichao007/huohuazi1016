# 为了避免模块名冲突，有引入了按目录来组织模块的方法

# 魔术方法
# class User():
#     pass
# if __name__ == '__main__':
#     print(dir(User())) # 列出魔术方法

# class User_A(object):
#     def __init__(self,name,age):
#         self.name = name 
#         self.age = age

# user = User_A('huohuazi1016',2)

# 创建一个类的过程是分两步的，一步是创建类的对象，还有一步就是对类进行初始化

# 对象的描述器
# class User(object):
#     def __init__(self,name = 'huohuazi1016',sex = 'boy'):
#         self.name = name
#         self.sex = sex
#     def __get__(self,obj,objtype):
#         print('获取name值')
#         return self.name
#     def __set__(self,obj,val):
#         print('设置name的值')
#         self.name = val
# class MyClass(object):
#     x = User('火华子','girl')
#     y = 5

# if __name__ =='__main__':
#     m = MyClass()
#     print(m.x)
#     print('\n')
#     m.x = 'libai'
#     print(m.x)
#     print('\n')
#     print(m.x)
#     print(m.y)

# 线程的创建
# import time
# import threading

# class MyThread(threading.Thread):
#     def run(self):
#         for i in range(5):
#             print('thread {},@number:{}'.format(self.name,i))
#             time.sleep(1)

# def main():
#     print('start main threading')
#     #创建线程
#     threads = [MyThread() for i in range(3)]
#     #启动三个线程
#     for t in threads:
#         t.start()
#     # 一次让新创建的线程执行join
#     # for t in threads:
#     #     t.join()
#     print('end main threading')

# if __name__ == '__main__':
#     main()

# 线程同步与互斥锁

    # 使用线程加载获取数据，通常都会造成数据不同步的情况。当然，我们可以给资源进行加锁，也就是
    # 访问资源的线程需要获得锁才能访问。
    # lock = threading.Lock()
    # 线程中获取锁
    # lock.acquire()
    # 完成后，释放锁
    # lock.release()
    # 为了支持在同一线程中多次请求同一资源，python提供了可重入锁（RLock）。RLock内部维护着一个Lock
    # 和一个counter变量，counter记录了acquire的次数，从而使得资源可以被多次require。直到一个线程
    # 所有的acquire都被release，其他的线程才能获得资源。

    # 创建重入锁
    # r_lock = threading.RLock()

# Condition 条件变量
    # 实用锁可以达到线程同步，在更复杂的环境，需要针对锁进行一些条件判断。
    # 使用Condition对象可以在某些事件出发或者达到特定的条件后才处理数据，Condition除了具有Lock对象
    # 的acquire方法和release方法外，还提供了wait和notify方法

    # 线程首先acquire一个条件变量锁，如果条件不足，则该线程wait，如果满足就执行线程，甚至可以notify
    # 其他线程。其他处于wait状态的线程接到通知后会重新判断条件。

    # 其中条件变量可以看成不同的线程先后acquire获得锁，如果不满足条件，可以理解为被扔到一个（Lock或RLock）
    # 的waiting池。直到其他线程notify之后在重新判断条件。不断重复这一过程，从而解决复杂的同步问题。

# import  threading,time 

# class Consumer(threading.Thread):
#     def __init__(self, cond,name):
#         #初始化
#         super(Consumer,self).__init__()
#         self.cond = cond
#         self.name = name 
#     def run(self):
#         # 确保先运行Seeker中的方法
#         time.sleep(1)
#         self.cond.acquire()
#         print(self.name + '两件商品一起，可以优惠吗？')
#         self.cond.notify()
#         self.cond.wait()
#         print(self.name + '已提交订单，帮忙修改一下价格？')
#         self.cond.notify()
#         self.cond.wait()
#         print(self.name + '收到，支付成功！')
#         self.cond.notify()
#         self.cond.release()
#         print(self.name + '收货')

# class Producer(threading.Thread):
#     def __init__(self, cond,name):
#         super(Producer,self).__init__()
#         self.cond = cond
#         self.name = name 
    
#     def run(self):
#         self.cond.acquire()
#         # 释放对锁的占用，同时线程挂起在这里，直到被notify并重新占有锁
#         self.cond.wait()
#         print(self.name + 'OK,提交订单吧！')
#         self.cond.notify()
#         self.cond.wait()
#         print(self.name + '好了，已经修改了')
#         self.cond.notify()
#         self.cond.wait()
#         print(self.name + 'OK,收款成功，马上发货')
#         self.cond.release()
#         print(self.name + '发货')

# cond = threading.Condition()
# consumer = Consumer(cond,'comsumer')
# producer = Producer(cond,'producer')
# consumer.start()
# producer.start()

# comsumer两件商品一起，可以优惠吗？
# producerOK,提交订单吧！
# comsumer已提交订单，帮忙修改一下价格？
# producer好了，已经修改了
# comsumer收到，支付成功！
# comsumer收货
# producerOK,收款成功，马上发货
# producer发货

# 线程间通信
    # 从一个线程向另一个线程发送数据最安全的方式就是使用queue库中的队列。创建一个被多个线程
    # 共享的queue对象，这些线程通过使用put（）和get（）操作向队列中添加或删除元素

# from queue import Queue
# from threading import Thread

# isRead = True

# def write(q):
#     #写数据进程
#     for value in ['huohuazi1016','火华子1016','libai']:
#         print('写进Queue的值为：{0}'.format(value))
#         q.put(value)
    
# def read(q):
#     #读数据进程
#     while isRead:
#         value = q.get(True)
#         print('从Queue读取的值为：{0}'.format(value))


# if __name__ == '__main__':
#     q = Queue()
#     t1 = Thread(target=write,args=(q,))
#     t2 = Thread(target=read,args=(q,))
#     t1.start()
#     t2.start()

# python 提供了Event对象用于线程间通信，它是线程设置的信号标志，如果信号标志为真，则其他线程等待
# 直到信号接触。
    # Event对象实现了简单的线程通信机制，它提供了设置信号，清除信号，等待信号用于实现线程间的通信
## 设置信号
    # 使用Event的set()方法可以设置Event对象内部的信号标志为真。Event对象提供了isSe()方法来判断其
    # 内部信号标志的状态。当使用event对象的set()方法后，isSet（）方法返回真
## 信号清除
    # 使用Event对象的clear（）方法可以清除Event对象内部的信号标志，即将其设为假，当使用Event的clear
    # 方法后，isSet（）方法返回假
## 等待
    # Event对象的wait的方法只有在内部信号为真的时候才会很快的执行并完成返回。当Event对象的内部信号
    # 标志位假时，则wait方法一直等待到其为真时返回

# import threading
# class mThread(threading.Thread):
#     def __init__(self,threadname):
#         threading.Thread.__init__(self,name = threadname)

#     def run(self):
#         #使用全局Event对象
#         global event
#         #判断Event对象内部信号标志
#         if event.isSet():
#             event.clear()
#             event.wait()
#             print(self.getName())
#         else:
#             print(self.getName())
#             #设置Event对象内部信号标志
#             event.set()
# #生成Event对象
# event = threading.Event()
# #设置Event对象内部信号标志
# event.set()
# t1=[]
# for i in range(10):
#     t = mThread(str(i))
#     #生成线程列表
#     t1.append(t)
# for i in t1:
#     #运行线程
#     i.start()
