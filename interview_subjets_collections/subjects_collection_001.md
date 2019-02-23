## 基本概念
    1. 1Gb = 10的9次方bytes (1Gb = 10亿字节)； 1Gb = 1024Mb, 1Mb = 1024Kb, 1Kb = 1024bytes;
    2. 基本流程：分解大问题，解决小问题，从局部最优选择全局最优；当然能够直接放进内存解决的那就直接想办法求解，不需要分解了。
    3. 分解过程常用方法： hash(x)%m, 其中x为字符串/url/ip， m为最小问题的数目。比如吧一个大文件分解为999份，那么m=999.
    4. 解决问题辅助数据结构：hash_map, Trie树，bit map, 二叉排序树（AVL,SBT,红黑树）
    5. top K 问题： 最大K个用最小堆，最小K个用最大堆。
    6. 处理大数据重用排序：快速排序， 堆排序，归并排序，桶排序
    
    