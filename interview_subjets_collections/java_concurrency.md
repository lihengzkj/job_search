1. Java多线程同步方法
    1. 使用同步代码
        1. 同步方法 public synchronized void methodName
        2. 同步代码块 synchronized (this) {...}
    2. 使用特殊域变量(volatile)实现线程同步
        1. volatile关键字为域变量的访问提供了一中免锁的机制
        2. 使用volatile修饰相当于告诉JVM该域可能会被其他的线程更新
        3. 因此每次使用该域就要重新计算，而不是使用寄存器中的值
        4. volatile不会提供任何的原子操作，他不能用来修饰final类型的变量
    3. 使用重入锁实现线程同步
        1. java.util.concurrent包来支持同步
        2. ReentrantLock 类是可重入，互斥，实现了Lock接口的锁，它和使用synchronized方法具有基本相同的语义和行为。
        3. ReentrantLock有两个方法lock 和 unlock来获取和释放锁。
        4. ReentrantLock()还有一个可以创建公平锁的构造方法，但是由于会大幅降低程序运行的效率，不推荐。
    4. 使用局部变量实现线程同步
        1. 使用ThreadLocal来实现
    5. 使用阻塞队列来实现线程的同步
        1. java.util.concurrent包中的 LinkedBlockingQueue<E> 可以实现线程同步
    6. 使用原子变量可以实现线程同步
        1. 原子操作就是指将读取变量值、修改变量值、保存变量值看成一个整体来操作即-这几种行为要么同时完成，要么都不完成。
        2. java的util.concurrent.atomic包中提供了创建了原子类型变量的工具类
        3. 比如其中AtomicInteger 表可以用原子方式更新int的值。 AtomicInteger常用方法：
           AtomicInteger(int initialValue) : 创建具有给定初始值的新的。 
           AtomicIntegeraddAddGet(int dalta) : 以原子方式将给定值与当前值相加。
           get() : 获取当前值
        4. 原子操作主要有：对于引用变量和大多数原始变量(long和double除外)的读写操作；
           对于所有使用volatile修饰的变量(包括long和double)的读写操作。