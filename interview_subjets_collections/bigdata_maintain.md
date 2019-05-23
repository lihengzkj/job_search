1. https://www.jianshu.com/p/62c5fe3e459f
2. HDFS常见的数据压缩格式有哪些，介绍其中一种详细的实现方式
    1. 常见的压缩格式
        1. TEXTFILE　　　 默认格式
        2. RCFILE　　　　　hive 0.6.0 和以后的版本
        3. ORC　　　　　　 hive 0.11.0 和以后的版本
        4. PARQUET　　　　 hive 0.13.0 和以后的版本,该数据格式企业中最常用
        5. AVRO　　　　　　hive 0.14.0 和以后的版本
    2. 数据存储的方式
        1. 按行存储 textfile
        2. 按列存储 orc/parqurt
            1. --orcfile 每列数据有类似于元数据的索引信息,可以确定列内容,需要某列信息时可以直接锁定列内容,
            效率优于按行存储压缩出来的文件比例最小,以时间换存储
            2. 比较复杂,支持嵌套数据结构和高效其种类丰富的算法(以应对不同值分布特征的压缩).压缩率不如orcfile,时间与压缩比适中
            
3. HDFS垃圾回收的时间模式是多久，如何修改该时间
    1. HDFS的垃圾回收  的默认配置的 0，也就是说，如果你不小心误删除了某样东西，那么这个操作是不可恢复的。
    2. 但是如果配置了HDFS的垃圾回收机制，那么删除的东西就可以在垃圾箱中保存一段你配置的时间，等时间过了在执行删除操作
    3. 配置文件所在位置 :hadoop安装目录/etc/hadoop/core-site.xml 
    4. 配置文件
     ```abc
     <property>
        <name>fs.trash.interval</name>
        <value>10080</value>
    </property>
     ```
4. HDFS如何生效机架感知，取消机架感知有什么问题
5. HDFS常见的运维操作有哪些，哪些操作是高危的，如果高危操作出现问题，如何解决
    
6. HDFS常见的故障是什么，如何处理，是否可以给出三种预案来防范大部分常见故障
    1. 权限问题。比如hdfs需要写入目录的权限不足，本地目录工作异常,(权限问题)，
        出现异常后大家不要看到一堆错误代码就心慌，不必害怕。
        hadoop目录下有个日志文件夹. 如果那个节点 出现问题就查看日志信息。 
        `tail  -F  /XXX.log`    tail -F 可以动态监控文件内容的变化。
    2. 文件属主不一致。比如文件是普通用户修改的或者文件没有相应的权限。
        root用户就无法实现读取或写入功能。 可以用文件所有者赋予权限:  `chown  +  username xxx.`
    3. 比如上传文件，报错。NameNode is  safe mode.   
        这是因为集群处于安全模式下,安全模式下禁止对文件的任何操作，包括写and 删除等操作。这时候需要退出安全模式。
        退出安全模式的命令:  `hdfs  dfsadmin  -safemode  leave`  
        查看集群的状态信息   `hdfs   dfsadmin   -report`  
    4. 启动start-dfs.sh 后上传文件，发现上传失败。报异常错误。就尝试把tmp目录删除后重新格式化。 hadoop   namenode  -format 
    5. 如果进程不存在,就查看相关进程日志文件来分析错误。
        如果进程存在还是有问题，可能是进程间的集群协调有问题。可以通过查看集群的报告信息。  
        `hdfs  dfsadmin   -report`
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
    设置hdfs-site.xml下面的属性值:
    ```aa
    <property>
        <name>dfs.block.size</name>
        <value>134217728</value>    --修改为128M
        <description>Block size</description>
    </property>
    ```
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
    
30. 有两个hadoop集群，机器相同，磁盘占用相同，一个集群磁盘的使用率比较均匀，
    另一个集群磁盘使用率起伏较大（很多写满的，很多使用率很低的），那么第二个集群会有哪些问题
    
31. hdfs namenode启动慢，常见的原因有哪些？如何优化？
    
32. hadoop的hdfs、yarn配置的zookeeper，是否可以分开
    
33. Sqoop用起来感觉怎样  
    说实话，Sqoop在导入数据的速度上确实十分感人，通过进一步了解，发现Sqoop1和Sqoop2在架构上还是有明显不同的，
    无论是从数据类型上还是从安全权限，密码暴露方面，Sqoop2都有了明显的改进，同时同一些其他的异构数据同步工具比较,
    如淘宝的DataX或者Kettle相比，Sqoop无论是从导入数据的效率上还是从支持插件的丰富程度上，Sqoop还是相当不错滴！！
    
34. ZooKeeper的角色以及相应的Zookepper工作原理？  
    Zookeeper的角色大概有如下四种：leader、learner（follower）、observer、client。
    其中leader主要用来决策和调度，follower和observer的区别仅仅在于后者没有写的职能，
    但都有将client请求提交给leader的职能，而observer的出现是为了应对当投票压力过大这种情形的，
    client就是用来发起请求的。而Zookeeper所用的分布式一致性算法包括leader的选举其实和-原始部落的获得神器为酋长，
    或者得玉玺者为皇帝类似，谁id最小，谁为leader，会根据你所配置的相应的文件在相应的节点机下生成id，
    然后相应的节点会通过getchildren（）这个函数获取之前设置的节点下生成的id，
    谁最小，谁是leader。并且如果万一这个leader挂掉了或者堕落了，则由次小的顶上。
    而且在配置相应的zookeeper文件的时候回有类似于如下字样的信息：
    Server.x=AAAA:BBBB:CCCC。其中的x即为你的节点号哈，AAAA对应你所部属zookeeper所在的ip地址，
    BBBB为接收client请求的端口，CCCC为重新选举leader端口。
35. HBase的Insert与Update的区别？  
    当时实现的与hbase交互的三个方法分别为insert、delete、update。
    由于那个项目是对接的一个项目，对接的小伙伴和我协商了下，不将update合并为insert，
    如果合并的话，按那个项目本身，其实通过insert执行overwrite相当于间接地Update，
    本质上，或者说在展现上是没什么区别的包括所调用的put。但那仅仅是就着那个项目的程序而言，
    如果基于HBase shell层面。将同一rowkey的数据插入HBase，其实虽然展现一条，但是相应的timestamp是不一样的，
    而且最大的版本数可以通过配置文件进行相应地设置。
    
36. HBase和Hive都是基于Hadoop，为什么Hive查询起来非常慢，但HBase不是？  
    Hive是类SQL引擎，其查询都需要遍历整张表，跑MapReduce自然很慢，
    但HBase是一种NoSQL的列式数据库，基于Key/Value的存储格式，不需要像Hive一样遍历，自然在速度上，乃至写的性能上是相当之快的。
    
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
    
38. HDFS的存储机制
    1. 读取机制
        1. 客户端向namenode请求上传文件，namenode检查目标文件是否已存在，父目录是否存在。
        2. namenode返回是否可以上传。
        3. 客户端请求第一个 block上传到哪几个datanode服务器上。
        4. namenode返回3个datanode节点，分别为dn1、dn2、dn3。
        5. 客户端请求dn1上传数据，dn1收到请求会继续调用dn2，然后dn2调用dn3，将这个通信管道建立完成
        6. dn1、dn2、dn3逐级应答客户端
        7. 客户端开始往dn1上传第一个block（先从磁盘读取数据放到一个本地内存缓存），以packet为单位，dn1收到一个packet就会传给dn2，
        dn2传给dn3；dn1每传一个packet会放入一个应答队列等待应答
        8. 当一个block传输完成之后，客户端再次请求namenode上传第二个block的服务器。（重复执行3-7步）
    2. 下载机制：
        1. 客户端向namenode请求下载文件，namenode通过查询元数据，找到文件块所在的datanode地址。
        2. 挑选一台datanode（就近原则，然后随机）服务器，请求读取数据。
        3. datanode开始传输数据给客户端（从磁盘里面读取数据放入流，以packet为单位来做校验）。
        4. 客户端以packet为单位接收，先在本地缓存，然后写入目标文件。
 39. secondarynamenode工作机制
    1. 第一阶段：namenode启动
        1. 第一次启动namenode格式化后，创建fsimage和edits文件。如果不是第一次启动，直接加载编辑日志和镜像文件到内存
        2. 客户端对元数据进行增删改的请求
        3. namenode记录操作日志，更新滚动日志。
        4. namenode在内存中对数据进行增删改查
    2. 第二阶段：Secondary NameNode工作
        1. SecondaryNameNode询问namenode是否需要checkpoint。直接带回namenode是否检查结果。
        2. SecondaryNameNode请求执行checkpoint。
        3. namenode滚动正在写的edits日志
        4. 将滚动前的编辑日志和镜像文件拷贝到Secondary NameNode
        5. SecondaryNameNode加载编辑日志和镜像文件到内存，并合并。
        6. 生成新的镜像文件fsimage.chkpoint
        7. 拷贝fsimage.chkpoint到namenode
        8. namenode将fsimage.chkpoint重新命名成fsimage
        
 40. NameNode与SecondaryNameNode 的区别与联系
    1. 区别
        1. NameNode负责管理整个文件系统的元数据，以及每一个路径（文件）所对应的数据块信息
        2. SecondaryNameNode主要用于定期合并命名空间镜像和命名空间镜像的编辑日志。
    2. 联系
        1. SecondaryNameNode中保存了一份和namenode一致的镜像文件（fsimage）和编辑日志（edits）
        2. 在主namenode发生故障时（假设没有及时备份数据），可以从SecondaryNameNode恢复数据
        
 41. hadoop节点动态上线下线怎么操作
    1. 上线
        1. 当要新上线数据节点的时候，需要把数据节点的名字追加在 dfs.hosts 文件中
        2. 关闭新增节点的防火墙
        3. 在 NameNode 节点的 hosts 文件中加入新增数据节点的 hostname
        4. 在每个新增数据节点的 hosts 文件中加入 NameNode 的 hostname
        5. 在 NameNode 节点上增加新增节点的 SSH 免密码登录的操作
        6. 在 NameNode 节点上的 dfs.hosts 中追加上新增节点的 hostname,
        7. 在其他节点上执行刷新操作：hdfs dfsadmin -refreshNodes
        8. 在 NameNode 节点上，更改 slaves 文件，将要上线的数据节点 hostname 追加到 slaves 文件中
        9. 启动 DataNode 节点
        10. 查看 NameNode 的监控页面看是否有新增加的节点
    2. 下线
        1. 修改/conf/hdfs-site.xml 文件
        2. 确定需要下线的机器，dfs.osts.exclude 文件中配置好需要下架的机器，这个是阻止下架的机器去连接 NameNode。
        3. 配置完成之后进行配置的刷新操作./bin/hadoop dfsadmin -refreshNodes,这个操作的作用是在后台进行 block 块的移动。
        4. 当执行三的命令完成之后，需要下架的机器就可以关闭了，可以查看现在集群上连接的节点，正在执行 Decommission，
           会显示：Decommission Status : Decommission in progress 执行完毕后，会显示：Decommission Status :Decommissioned
        5. 机器下线完毕，将他们从excludes 文件中移除。
        
42. HAnamenode是如何工作的（ZKFailoverController主要职责）
    1. 健康监测：周期性的向它监控的NN发送健康探测命令，从而来确定某个NameNode是否处于健康状态，
        如果机器宕机，心跳失败，那么zkfc就会标记它处于一个不健康的状态。
    2. 会话管理：如果NN是健康的，zkfc就会在zookeeper中保持一个打开的会话，
        如果NameNode同时还是Active状态的，那么zkfc还会在Zookeeper中占有一个类型为短暂类型的znode，
        当这个NN挂掉时，这个znode将会被删除，然后备用的NN，将会得到这把锁，升级为主NN，同时标记状态为Active。
    3. 当宕机的NN新启动时，它会再次注册zookeper，发现已经有znode锁了，
        便会自动变为Standby状态，如此往复循环，保证高可靠，需要注意，目前仅仅支持最多配置2个NN。
    4. master选举：如上所述，通过在zookeeper中维持一个短暂类型的znode，来实现抢占式的锁机制，从而判断那个NameNode为Active状态
    