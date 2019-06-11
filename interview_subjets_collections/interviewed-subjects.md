## 基本概念
    1. 1Gb = 10的9次方bytes (1Gb = 10亿字节)； 1Gb = 1024Mb, 1Mb = 1024Kb, 1Kb = 1024bytes;
    2. 基本流程：分解大问题，解决小问题，从局部最优选择全局最优；当然能够直接放进内存解决的那就直接想办法求解，不需要分解了。
    3. 分解过程常用方法： hash(x)%m, 其中x为字符串/url/ip， m为最小问题的数目。比如吧一个大文件分解为999份，那么m=999.
    4. 解决问题辅助数据结构：hash_map, Trie树，bit map, 二叉排序树（AVL,SBT,红黑树）
    5. top K 问题： 最大K个用最小堆，最小K个用最大堆。
    6. 处理大数据重用排序：快速排序， 堆排序，归并排序，桶排序
    
    
 ## shensi 
    1. HashMap, HashTable,ConcurrentHashMap的区别
    2. short s1 = 1; s1 = s1 +1; wrong or right? why ?
    3. 关系数据库和非关系数据库的区别，什么是列数据库，具体应用场景是什么？
    4. Describle HDFS HA
    5. kafka 的数据是存内存还是存盘? 为什么吞吐量大? 怎么保证数据不丢失?
    6. 描述HBase一条数据的写入过程
    7. 解决HBase表在初始写入的时候热度热写的问题?
    8. 解决Redis的服务器突然断电的数据丢失问题?
    9. 如何避免HDFS的小文件问题
    
## hongli 
    1. 怎么防止spark的内存泄漏的问题
    2. 怎么处理数据倾斜
    3. 列出所知道的spark的算子，并提出使用的建议
    4. 怎么促进Hive的查询？ 怎么设计表？
    5. 描述在做ETL过程中遇到的困难或者难点
    6. 描述Hadoop的各个组件
    7. 描述Hadoop的checkpoints
    
## kelai
    paper:
        bigdata:
            1.hdfs读写过程
            2. 任务运行on yarn的原理
            3. 如何用MapReduce完成单词的去重
            4. hbase查询实现的内部原理
            5. hadoop的安装步骤
            6. hadoop的角色分配以及功能
            7. jps命令的用处
            8. hdfs的写流程
        OPS：
            1. docker容器存储驱动overlay和overlay2的主要区别
            2.容器内部访问容器外部网络的实现原理
            3.三条dockerfile的最佳实践
            4. dockerfile指令中RUN,CMD,ENTRYPOINT的区别以及最佳实践
    face-to-face:
        1. 集群规模
        2. 数据量
        3. spark的运行原理
        4. 宽依赖和窄依赖
        5. 具体业务流程