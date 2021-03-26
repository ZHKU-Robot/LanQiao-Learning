# 2018年第九届C/C++ A组蓝桥杯省赛真题

### 目录

- - - [第一题：哪天返回](https://blog.csdn.net/kiwi_berrys/article/details/111463526#_7)
        - [第二题：猴子分香蕉](https://blog.csdn.net/kiwi_berrys/article/details/111463526#_24)
        - [第三题：字母阵列](https://blog.csdn.net/kiwi_berrys/article/details/111463526#_44)
        - [第四题：第几个幸运数](https://blog.csdn.net/kiwi_berrys/article/details/111463526#_175)
        - [第五题：书号验证](https://blog.csdn.net/kiwi_berrys/article/details/111463526#_198)
        - [第六题：稍小分数](https://blog.csdn.net/kiwi_berrys/article/details/111463526#_243)
        - [第七题：次数差](https://blog.csdn.net/kiwi_berrys/article/details/111463526#_298)
        - [第八题：等腰三角形](https://blog.csdn.net/kiwi_berrys/article/details/111463526#_337)
        - [第九题：小朋友崇拜圈](https://blog.csdn.net/kiwi_berrys/article/details/111463526#_433)
        - [第十题：耐摔指数](https://blog.csdn.net/kiwi_berrys/article/details/111463526#_477)

## 第一题：哪天返回

### 题目描述

小明被不明势力劫持。后莫名其妙被扔到x星站再无问津。小明得知每天都有飞船飞往地球，但需要108元的船票，而他却身无分文。
他决定在x星战打工。好心的老板答应包食宿，第1天给他1元钱。
并且，以后的每一天都比前一天多2元钱，直到他有足够的钱买票。
请计算一下，小明在第几天就能凑够108元，返回地球。

要求提交的是一个整数，表示第几天。请不要提交任何多余的内容。

### 题目分析

..常规送分中

### 题目代码

```
i=1;
count=1
while i<108:
    print(i)
    i+=i+2
    count+=1
    
print(count)

```

## 第二题：猴子分香蕉

### 题目描述

5只猴子是好朋友，在海边的椰子树上睡着了。这期间，有商船把一大堆香蕉忘记在沙滩上离去。
第1只猴子醒来，把香蕉均分成5堆，还剩下1个，就吃掉并把自己的一份藏起来继续睡觉。
第2只猴子醒来，重新把香蕉均分成5堆，还剩下2个，就吃掉并把自己的一份藏起来继续睡觉。
第3只猴子醒来，重新把香蕉均分成5堆，还剩下3个，就吃掉并把自己的一份藏起来继续睡觉。
第4只猴子醒来，重新把香蕉均分成5堆，还剩下4个，就吃掉并把自己的一份藏起来继续睡觉。
第5只猴子醒来，重新把香蕉均分成5堆，哈哈，正好不剩！

请计算一开始最少有多少个香蕉。

需要提交的是一个整数，不要填写任何多余的内容。

### 题目分析

这道题很像那个什么,忘记了,反正无脑取余爆破

原本是5堆 的 取余5后 余1 然后藏起来自己一份 

剩下4堆

剩下的4堆 取5份 余 2 然后藏起来一份

..



### 题目代码


