1. https://www.jianshu.com/p/62c5fe3e459f
2. HDFS常见的数据压缩格式有哪些，介绍其中一种详细的实现方式
3. HDFS垃圾回收的时间模式是多久，如何修改该时间
4. HDFS如何生效机架感知，取消机架感知有什么问题
5. HDFS常见的运维操作有哪些，哪些操作是高危的，如果高危操作出现问题，如何解决
6. HDFS常见的故障是什么，如何处理，是否可以给出三种预案来防范大部分常见故障
7. 你经历过哪些严重的Hadoop故障
8. HDFS常用的IO压力测试工具有哪些
9. Hadoop哪些地方依赖于主机名，是否可以全部替换为IP呢（HDFS/YARN/SPARK）
10. HDFS有哪些核心的指标需要采集和监控，最重要的三个指标是什么
11. HDFS节点下线，如何提升其下线速度
12. HDFS常见的误删除数据场景，以及如何防止数据被误删除
13. HDFS集群对外提供的访问方式有几种，哪种最为常见，每种方式各自的优缺点和使用场景
14. HDFS你做过哪些性能调优，哪些是通用的，哪些是针对特定场景的
15. Hadoop日常的运维操作有什么管理工具，已经搭建的集群如何使用ambari
16. Hadoop各类角色如何进行扩容，缩容，节点迁移（IP变更）
17. Hadoop各类角色的JVM参数配置如何设定
18. HDFS的block大小如何设置，取决于哪些因素
19. YARN的nodemanager上跑任务的时候，有时候会将磁盘全部打满，如何解决
20. HDFS集群多个业务方使用时如何提前做好运维规划，如权限，配额，流量突增，数据安全，目录结构
21. HDFS中，小文件的定义是什么，如何对小文件进行统计分析，如何优化该问题
22. HDFS的namenode如何进行主备切换
23. YARN的nodemanager导致机器死机，如何解决
24. 如何下线YARN的nodemanager节点，假如该节点持续在运行计算任务
25. YARN的nodemanager节点，从Active Nodes转为Lost Nodes，有哪些原因，在哪里设置
26. YARN的nodemanager节点如果转为Lost Nodes后，该节点上的计算任务是否还会正常继续
27. HDFS的快照原理简要介绍一下，为什么可以确保数据的安全性
28. YARN的yarn.nodemanager.local-dirs和yarn.nodemanager.log-dirs参数应该如何设置，有哪些常见的问题
29. distcp拷贝数据的时候，出现了java.lang.outofmemoryerror:java heap space，如何处理
30. 有两个hadoop集群，机器相同，磁盘占用相同，一个集群磁盘的使用率比较均匀，另一个集群磁盘使用率起伏较大（很多写满的，很多使用率很低的），那么第二个集群会有哪些问题
31. hdfs namenode启动慢，常见的原因有哪些？如何优化？
32. hadoop的hdfs、yarn配置的zookeeper，是否可以分开

33. Sqoop用起来感觉怎样  
    说实话，Sqoop在导入数据的速度上确实十分感人，通过进一步了解，发现Sqoop1和Sqoop2在架构上还是有明显不同的，无论是从数据类型上还是从安全权限，密码暴露方面，Sqoop2都有了明显的改进，同时同一些其他的异构数据同步工具比较,如淘宝的DataX或者Kettle相比，Sqoop无论是从导入数据的效率上还是从支持插件的丰富程度上，Sqoop还是相当不错滴！！
34. ZooKeeper的角色以及相应的Zookepper工作原理？  
    Zookeeper的角色大概有如下四种：leader、learner（follower）、observer、client。其中leader主要用来决策和调度，follower和observer的区别仅仅在于后者没有写的职能，但都有将client请求提交给leader的职能，而observer的出现是为了应对当投票压力过大这种情形的，client就是用来发起请求的。而Zookeeper所用的分布式一致性算法包括leader的选举其实和-原始部落的获得神器为酋长，或者得玉玺者为皇帝类似，谁id最小，谁为leader，会根据你所配置的相应的文件在相应的节点机下生成id，然后相应的节点会通过getchildren（）这个函数获取之前设置的节点下生成的id，谁最小，谁是leader。并且如果万一这个leader挂掉了或者堕落了，则由次小的顶上。而且在配置相应的zookeeper文件的时候回有类似于如下字样的信息：Server.x=AAAA:BBBB:CCCC。其中的x即为你的节点号哈，AAAA对应你所部属zookeeper所在的ip地址，BBBB为接收client请求的端口，CCCC为重新选举leader端口。
35. HBase的Insert与Update的区别？  
    当时实现的与hbase交互的三个方法分别为insert、delete、update。由于那个项目是对接的一个项目，对接的小伙伴和我协商了下，不将update合并为insert，如果合并的话，按那个项目本身，其实通过insert执行overwrite相当于间接地Update，本质上，或者说在展现上是没什么区别的包括所调用的put。但那仅仅是就着那个项目的程序而言，如果基于HBase shell层面。将同一rowkey的数据插入HBase，其实虽然展现一条，但是相应的timestamp是不一样的，而且最大的版本数可以通过配置文件进行相应地设置。
36. HBase和Hive都是基于Hadoop，为什么Hive查询起来非常慢，但HBase不是？  
    Hive是类SQL引擎，其查询都需要遍历整张表，跑MapReduce自然很慢，但HBase是一种NoSQL的列式数据库，基于Key/Value的存储格式，不需要像Hive一样遍历，自然在速度上，乃至写的性能上是相当之快的。
37. spark 资源的动态分配
    ```abc
    def conf(self):
     conf = super(TbtestStatisBase, self).conf
     conf.update({
            'spark.shuffle.service.enabled': 'true',
            'spark.dynamicAllocation.enabled': 'false',
            'spark.dynamicAllocation.initialExecutors': 50,
            'spark.dynamicAllocation.minExecutors': 1,
            'spark.dynamicAllocation.maxExecutors': 125,
            'spark.sql.parquet.compression.codec': 'snappy',
            'spark.yarn.executor.memoryOverhead': 4096,
            "spark.speculation": 'true',
            'spark.kryoserializer.buffer.max': '512m',
      })
     ```
    1、spark.shuffle.service.enabled。用来设置是否开启动态分配。开启了动态分配的Application在申请资源的时候默认会拥有更高的优先级  
    2、spark.dynamicAllocation.initialExecutors (默认下是3)  
    spark.dynamicAllocation.minExecutors (默认下是0)  
    spark.dynamicAllocation.maxExecutors (默认下是30)  
    Executor应该是所谓资源单位，自己理解为越多执行越快嘛，如果是Yarn的话，就是Containers，一个道理　　
    3、spark.yarn.executor.memoryOverhead 是设置堆外内存大小，和 executor_memory 做个对比：  
　　ExecutorMemory为JVM进程的JAVA堆区域。  
　　MemoryOverhead是JVM进程中除Java堆以外占用的空间大小，包括方法区（永久代）、Java虚拟机栈、本地方法栈、JVM进程本身所用的内存、直接内存（Direct Memory）等。  
　　两者关系：如果用于存储RDD的空间不足，先存储的RDD的分区会被后存储的覆盖。当需要使用丢失分区的数据时，丢失的数据会被重新计算。ExecutorMemory + MemoryOverhead之和（JVM进程总内存）  　　          　　　　             
     我只是简单理解堆外内存为一个备用区域吧，还不知道具体什么作用。有遇到内存不够报错的情况，然后调大了MemoryOverhead。  
    4、理论上：非动态分配情况下，我们必须要等到有100个Executor才能运行Application，并且这100个会一直被占用到程序结束，即便只有一个任务运行了很长时间。
    动态分配情况下，当有10个Executor的时候，我们的Application就开始运行了，并且我们后续可以继续申请资源，最多申请到100个Executor，当我们有空闲资源的时候，
    我们可以被释放资源到最少只保留10个Executor，当需要的时候我们有更高的优先级从YARN那儿拿到资源。
    
    