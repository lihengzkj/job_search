### spark 开发调优
    1. 避免重复创建RDD。 同一份数据源只应该创建一个RDD.
    
    2. 竟可能复用一个RDD, 减少RDD数量从而减少算子执行的次数。
    
    3. 多次使用的RDD应该进行持久化。RDD调用cache()和persist()即可。进行算子计算就不会重头计算而且从持久化的RDD进行计算。
    
    4. 尽量避免使用shuffle类算子，如reducerBykey, join, distinct, repartition等。
       在shuffle的过程中，可能发生大量的磁盘文件读写的IO操作，以及数据的网络传输操作。如果一定要使用join的话，
       最好是把较小的RDD(几百M或者一两个G)进行广播，让这个较小的RDD驻留在每个executor中，这样join就不会发生shuffle了。
    
    5. 使用map-site的预聚合的shuffle操作。所谓的map-site的预聚合，说的是在每个节点本地对相同的key进行一次聚合操作。
       map-site预聚合之后，每个节点本地就只会有一个相同的key，因为多条相同的key都被聚合起来了。其他节点在拉去所有
       节点上的相同的key的时候，就会大大减少需要拉取数据的数量，从而减少了磁盘IO以及网络传输的开销。通常来说，在可
       能的情况下，建议使用reduceByKey或者aggregateByKey算子来代替groupByKey算子。因为reduceByKey和aggregateByKey
       算子都会使用用户自定义的函数对每个节点本地相同的key进行预聚合。而groupByKey算子不会进行预聚合，全量的数据
       会在集群的各个节点之间分发和传输，性能相对比较差。
       
    6. 使用高性能的算子
        使用reduceByKey或者aggregateByKey 代替 groupByKey
        使用mapPartition 代替普通的map
        使用foreachPartition 代替普通的foreach
        使用filter之后进行coalesce操作
        使用repartitionAndSortWithinPartition 代替partition 与 sort类操作
        官方建议，如果需要在repartition重分区之后，还要进行排序，建议直接使用repartitionAndSortWithinPartitions算子。
        
    7. 广播大变量。对大变量进行广播会保证每个executor的内存中只有一份变量副本，而executor的task会共享这个副本，
       这样会减少副本的数量。如果不广播，每个task都会有一个变量副本。
       
    8. 使用Kryo优化序列化性能。spark涉及三个地方的序列化：
       a. 当在算子内部使用外部变量的时候，该变量会被序列化传给每个task。
       b. 将自定义的类作为RDD的泛型的时候，所有自定义的类型都会进行序列化。要求自定义类实现seriliaed接口
       c. 使用序列化的持久化机制策略的时候，e.g.MEMORY_ONLY_SER， spark会将RDD的每个partition都序列化为字节数组。
          Kryo序列化的性能是默认的Java的序列化的性能的10倍。
          
    9. 优化数据结构。三种数据结构比较消耗内存：
        a. Java对象，每个Java对象都有对象头，引用等额外的信息，因此比较占用内存空间。
        b. 字符串，每个字符串内部都有一个字符串数组以及长度等额外信息。
        c. 集合类型。集合类型内部通常使用一些内部类封装集合元素， e.g.Map.Entry
           官方建议尽量不要使用上述三种数据结构。尽量使用字符串数组代替对象，使用原始类型代替字符串，
           使用数组代替集合，尽可能减少内存的使用，降低gc频率。
           
### spark 资源调优  
    资源调优主要是进行参数的调优，具体如下：
    
    1. num-executors  job需要多少个executor来执行。可以根据资源情况和数据集的大小来计算合适的值。
    
    2. executor-memory  每个executor使用的内存大小
    
    3. executor-cores 每个executor使用的CUP的core的数量
    
    4. driver-memory  driver进程使用的内存大小。通常1G足够，但是当需要使用collect函数把RDD的数据拉取到driver上进行处理的
        时候就需要增大内存。
        
    5. spark.default.parallelism    每个stage默认的task数量。默认spark根据底层的HDFS的block数量来设置task的数量，一个HDFS
       的block对应一个task.通常默认的数量是偏少的。spark的官方建议设置该参数的值为executors * executor-cores 的 2到3倍。
      
    6. spark.sql.shuffle.partitions    spark默认使用的partition数量是200，这个参数通常来说是比较大的，造成资源浪费，我们
       可以适当的减少。
       
       
### spark RDD
    1. 概念  
        spark的核心概念就是RDD(resilient distributed dataset),指的是一个
        只读的,可分区的分布式数据集,这个数据集的全部或者部分可以缓存到内存中,
        在多次计算之间可以重用.  
        分区是RDD内部并行计算的一个计算单元,RDD的数据集在逻辑上被划分为多个分
        片,每个分片称为分区,分区的格式决定了并行计算的粒度,而每个分区的数值计算
        都是在一个任务中进行的,因此任务的个数,也就是RDD的分区数决定. 
  
    2. RDD的特点
        a. 是一个只读记录的集合: 状态不可变,不能修改  
        b. 一个具有容错机制的特殊集  
        c. 只能通过在稳定的存储器或其他的RDD上的确定性操作来创建.
        d. 分区: 支持使用RDD中的元素根据key来分区,保存到多个节点上.
            还原的时候只会重新计算丢失的分区的数据,而不会影响整个系统.  
        e. 路径; 在RDD中叫血统lineage, 即RDD有充足的信息关于它是如何
            从其他RDD产生而来的.
        f: 持久化: 支持将会被重用的RDD缓存(如in-memory或者溢出到磁盘)
        g: 延迟计算: spark会延迟计算RDD,使其能够管道化.
        h: 操作: 丰富的转换,tansformation , action.
        
    3. RDD弹性的特点
        a. 基于lineage的高效容错(第N个节点出错,会从第N+1个节点恢复,血统容错)
        b. task如果失败会自动进行特定次数的重试(默认4次)
        c. stage如果失败会自动进行特定次数的重试,只计算失败的数据分片.
        d. 数据弹性调度: DAG Task和资源无关
        e: checkpoint
        f: 自动的进行内存和磁盘数据存储的切换
        
    4. RDD的底层实现原理
        RDD是一个分布式数据集,其数据应该分部存储于多台机器上.事实上,每个RDD的数据
        都是以block的形式存储于多台机器上.看图,其中每个executor会启动一个
        blockManagerSlave并管理一部分block;而block的元数据有driver节点的
        blockManagerMaster保存.BlockManagerSlave生成block后向
        blockManagerMaster 注册该block, blockManagerMaster管理RDD和
        block的关系,当RDD不需要存储的时候将向blockManagerSlave发送指令
        删除相应的block.
    
    5. RDD的容错性机制
        
    
    6. RDD cache 和 persist的区别
        
    