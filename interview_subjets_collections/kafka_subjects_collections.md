### kafka如何保证消息的幂等性
    幂等producer： 保证发送单个分区的消息只会发送一次，不会出现重复消息。
    所谓幂等producer是指 producer.send的逻辑是幂等的，即发送相同的kafka消息，broker端不会重复写入消息。
    同一条消息，kafka保证底层日志中只会持久化一次，既不会丢失也不会重复。幂等性极大地减轻下游consumer
    系统消息去重的工作负担。  
    幂等producer提供的语义保证是有条件的：  
        1. 单分区幂等性： 幂等producer无法实现多分区的幂等性。如果要实现多分区的幂等性，需要引入实务。  
        2. 单会话的幂等性：幂等producer无法实现跨会话的幂等性。
        即使同一个producer宕机并重启也无法保证消息的EOS语义。  
      
     producer设计原理：  
     producer对象引入了一个新的字段： producer ID ，称PID， 它唯一标识了一个producer， 当producer启动时kafka，
     会为每一个producer分配一个PID(64位整数)， 因此PID的生成和分配对用户来说是完全透明的，用户无需考虑PI的
     事情，甚至都感受不到PID的存在。其次，从kafka 0.11开始，重构了消息的格式，引入了序列号字段sequence number
     来标识某个PID producer发送的消息。这个和consumer的offset类似，sequence number 从0开始计数并严格单调增加。
     这样每当PID发送新消息给broker时，broker就会对比这些信息，如果发生冲突(比如起始sequence number 和 结束的
     sequence number与当前的缓存不同)，那么broker就会拒绝这些消息的写入。如果没有冲突，那么broker就会更新这次
     的消息写入。这就是kafka producer的设计思路：  
        1. 为每个producer设计唯一的PID  
        2. 引入sequence number 以及broker端的sequence number 缓存更新机制来去重。
        
### kafka 的分区机制  
    Topic 在逻辑上可以被认为是一个queue，每条消息都必须指定topic，可以简单的理解为必须指明这条消息放入
    那个queue。 为了是kafka的吞吐率可以线性提高，物理上把topic分成一个或者多个partition，每个partition在
    物理上对应一个文件夹，该文件夹存储这个partition的所有的消息和索引文件。若创建topic1和topic2两个topic，
    且分别有13和19个分区，则整个集群上就会生成相应的32个文件夹。  
    
    因为kafka读取特定消息的时间复杂度是O(1)，即与文件大小无关，所以这里删除过期文件与提高kafka的效率无关。
    选择怎样的删除策略只与磁盘以及具体的需求有关。另外，kafka会为每一个consumerGroup保留一些metadata信息，
    这些信息是消费的partition，也就是offset。 这个offset有consumer控制。正常情况下consumer会在消费完一条消息
    以后增加该offset。当然，consumer也可将offset设成一个较小的值，重新消费一些消息。因为offset有consumer控制，
    所以kafka broker是无状态的，它不需要标记哪些消息是被哪些consumer消费过的，也不需要通过broker去保证同一个
    consumer Group 只有一个consumer能消费某一条消息，因此也就不需要锁机制，这是为kafka的高吞吐率提供了有力的保障。
    
### kafka consumer 的 rebalance机制：
    kafka保证同一个consumer group 中只有一个consumer会消费某条消息， 实际上，kafka保证的是稳定状态下每一个
    consumer实例只会消费一个或者多个特定的partition的数据。而某个partition的数据只会某一个特定的consumer实例
    所消费。也就是说kafka对消息的分配是以partition为单位分配的，而不是以每一条消息作为分配单元。这样的设计
    的劣势就是无法保证同一个consumer group 里的consumer均匀消费数据，优势是每一个consumer不用和大量的broker
    通信，减少通信的开销，同时也降低了分配的难度，实现也更简单。  
    
    另外，因为一个partition里面的数据是有序的，这种设计可以保证每个partition里的的数据被有序的消费。如果
    consumer group中consumer数量少于partition的数量，则至少有一个consumer会消费多个partition的数据， 如果consumer
    的数量与partition的数量相同，则正好一个consumer消费一个partition里的数据。而如果consumer的数量多于partition
    的数量，那么就会有部分的consumer无法消费到改topic下的任一条消息。  
    
    consumer rebalance的算法如下：  
        1. 将目标topic下所有的partition排序，存于partition（PT）。  
        2. 对某consumer group 下所有的consumer排序，存于consumer group（CG），第i个consumer记为Ci  
        3. N=size(PT)/size(CG)，向上取整  
        4. 解除Ci对原来partition的消费权（i从0开始）  
        5. 将第i*N 到 (i+1)*N-1个partition分配给Ci    
        
    每一个consumer或者broker的增加或者减少都会触发consumer的rebalance。因为每一个consumer只负责调整自己所消费的
    partition，为了保证整个consumer group的一致性，当一个consumer触发了Rebalance时，该consumer group内的其他所有
    的consumer也应该触发Rebalance。
        
### kafka 的特性
    1. 分布式，基于发布/订阅的消息系统
    2. 时间复杂度为O(1)的方式提供消息持久化能力，即使对TB级以上的数据也能保证正常时间复杂度的访问性能
    3. 高吞吐率。即使在廉价的商用机上也能做到单机支持每秒100K条以上的消息传输
    4. 支持 kafka server之间的消息分区，及分布式消费，同时保证每个partition内的消息顺序传输
    5. 同时支持离线数据处理和实时数据处理
    6. 支持在线性水平扩展
    
### kafka producer的消息路由
    producer发送消息到broker时，会根据partition机制选择其存储到哪一个partition。如果partition机制设置合理，所有消息
    可以均匀分布到不同的partition里，这样就实现了负载均衡。如果一个topic对应一个文件，那这个文件所在的机器IO将会成为
    这个topic的性能瓶颈，而有了partition以后，不同的消息可以并行写入不同的broker的不同的partition，极大提高了吞吐率。
    可以在#KAFKA_HOME/config/server.properties中通过配置num.partitions来指定新建topic的more的partition的数量，也可以
    在创建topic的时候进行参数指定，同时也可以在topic创建之后通过kafka工具修改。  
    
    在发送一条消息时，可以指定这条消息的key，producer根据这个key和partition机制来判断应该将该条消息发送到那个partition。
    partition机制可以通过指定producer的partition.class这一参数来指定，该class必须实现kafka.producer.partition接口。
    e.g. key可以被解析为整数，将对应的整数和partition总数取余，该消息就会被发送到改数对应的partition。
    