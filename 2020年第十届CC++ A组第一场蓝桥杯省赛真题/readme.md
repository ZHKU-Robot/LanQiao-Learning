# 2020年第十届C/C++ A组第一场蓝桥杯省赛真题

### 目录

- - - [第一题：跑步训练](https://blog.csdn.net/kiwi_berrys/article/details/111463920#_7)
        - [第二题：合并检测](https://blog.csdn.net/kiwi_berrys/article/details/111463920#_21)
        - [第三题：分配口罩](https://blog.csdn.net/kiwi_berrys/article/details/111463920#_33)
        - [第四题：矩阵](https://blog.csdn.net/kiwi_berrys/article/details/111463920#_44)
        - [第五题：完美平方数](https://blog.csdn.net/kiwi_berrys/article/details/111463920#_56)
        - [第六题：解码](https://blog.csdn.net/kiwi_berrys/article/details/111463920#_68)
        - [第七题：走方格](https://blog.csdn.net/kiwi_berrys/article/details/111463920#_82)
        - [第八题：整数小拼接](https://blog.csdn.net/kiwi_berrys/article/details/111463920#_96)
        - [第九题：超级胶水](https://blog.csdn.net/kiwi_berrys/article/details/111463920#_108)
        - [第十题：网络分析](https://blog.csdn.net/kiwi_berrys/article/details/111463920#_122)

## 第一题：跑步训练

### 题目描述

小明要做一个跑步训练。 初始时，小明充满体力，体力值计为 10000。如果小明跑步，每分钟损耗600的体力。如果小明休息，每分钟增加 300 的体力。体力的损耗和增加都是均匀变化的。
小明打算跑一分钟、休息一分钟、再跑一分钟、再休息一分钟……如此循环。如果某个时刻小明的体力到达0，他就停止锻炼。 请问小明在多久后停止锻炼。
为了使答案为整数，请以秒为单位输出答案。 答案中只填写数，不填写单位。

### 题目分析

做过了 参考  [README.md](../第十一届蓝桥杯python组/README.md) 

### 题目代码

## 第二题：合并检测

### 题目描述

新冠疫情由新冠病毒引起，最近在A国蔓延，为了尽快控制疫情，A国准备给大量民众进病毒核酸检测。
然而，用于检测的试剂盒紧缺。 为了解决这一困难，科学家想了一个办法：合并检测。即将从多个人（k个）采集的标本放到同一个试剂盒中进行检测。如果结果为阴性，则说明这k个人都是阴性，用一个试剂盒完成了 k 个人的检测。如果结果为阳性，则说明 至少有一个人为阳性，需要将这 k 个人的样本全部重新独立检测（从理论上看， 如果检测前 k−1 个人都是阴性可以推断出第 k 个人是阳性，但是在实际操作中 不会利用此推断，而是将 k 个人独立检测），加上最开始的合并检测，一共使用 了 k + 1 个试剂盒完成了 k 个人的检测。 A 国估计被测的民众的感染率大概是 1%，呈均匀分布。请问 k 取多少能最节省试剂盒？

### 题目分析

看不懂题

### 题目代码

------------------------------------------------
## 第三题：分配口罩

### **题目描述**

 某市市长获得了若干批口罩，给定每批口罩的数量，市长要把口罩分配给市内的2所医院。由于物流限制，每一批口罩只能全部分配给其中一家医院。市长希望2所医院获得的口罩总数之差越小越好。 请你计算这个差最小是多少？

###  **题目分析**

贪婪

###  **题目代码**