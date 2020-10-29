# [LeetCode-learning](https://leetcode-cn.com/problemset/all/)

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/ZHKU-Robot/Robot-algorithm-learning)

一起去LeetCode刷题吧~~欢迎clone到本地修改并pull

 ![发现事情并不简单](img/20201026689124_bqzonA.jpg) 

***
本仓库包含以下内容：

1. 现在只有yujiecong的单人solo

**注：目前的顺序为简单难度从上到下**

![1603720038896](img/1603720038896.png)

## 内容列表
- [前言](#前言)
- [失败](#失败)
- [更新](#更新)
- [目录](#目录)
- [背景](#背景)
- [相关仓库](#相关仓库)
- [维护者](#维护者)
- [如何贡献](#如何贡献)
- [使用许可](#使用许可)
## 前言
很痛苦,如果不熟悉排序算法，你可能会半天憋不出一个代码或者说半天调试不对代码..  
所以请确保你对以下算法熟悉.

- 直接插入排序(哨兵位)
- 冒泡排序(以及进阶冒泡)
- 递归(我也不会呜呜呜)
- 动态规划
- 常用数据结构的增删改查
    - 链表 √
    - 栈 √
    - 队列 ×
    - 二叉树 ×
## 失败
记录一下没做出来的题
-  [climbing-stairs](Easy\climbing-stairs) 
    - 动态规划(dp)
    - 滚动数组
    - 递归
    - 找规律(斐波那契数列)
- [Maximum Subarray](./Easy/maximum-subarray)
    - 滚动数组
    - 动态规划
    - 贪心算法
    - 分治法
## 更新
- 2020年10月29日21:50:59 yujiecong更不动了，当我看见二叉树，没动力了
    - 淦
- 2020年10月28日21:36:40 yujiecong更新   [merge-sorted-array](Easy\merge-sorted-array) 
    - 直接插入排序
- 2020年10月28日13:30:48 yujiecong更新  [remove-duplicates-from-sorted-list](Easy\remove-duplicates-from-sorted-list) 
    - 20分钟（很不满意)
    - 链表的删除
- 2020年10月27日22:19:36 yujiecong更新   [climbing-stairs](Easy\climbing-stairs) 
    - 又出现一道不会做的题了
    - 动态规划(DP)
    - 递归
    - 找规律(斐波那契数列)
    - 已收藏
- 2020年10月26日23:28:46 yujiecong 更新  [sqrtx](Easy\sqrtx) 
    - 作弊都能过笑死我了
    - 5s做出
    - 待完善完整的sqrt实现
- 2020年10月26日23:23:40 yujieocng 更新 [add-binary](Easy\add-binary) 
    - 1分钟做出
- 2020年10月26日23:16:12 yujiecong更新 [plus-one](Easy\plus-one) 
    - 3分钟做出
- 2020年10月26日17:28:54 yujiecong更新 [length-of-last-word](Easy\length-of-last-word) 
    - 耗时42分钟，不是很满意
        - 极端情况
        - 过滤脏数据
        - 倒序查找
- 2020年10月25日23:32:26 yujiecong更新[Maximum Subarray](./Easy/maximum-subarray)却想不出来(建议收藏)
    - 动态规划
    - 贪心算法
    - 分治法
    - 看到这题难度为简单，我陷入了沉思! 
        - 思考了30分钟我一行代码没写出来，我又陷入了沉思！
        - 看了参考思路终于明白后，我又陷入了沉思！
            - 建议复习!
- 2020年10月25日15:24:23 yujiecong更新[外观数列](./Easy/count-and-say/)
    - 昨天没更新，今天冒个泡,这道题是我第一次看一遍没看懂的简单题，记录一下哈哈
        - 找出内在规律
        - 合适的判断以及结束条件
        - 递归与for循环转换
- 2020年10月23日23:05:01 yujiecong**完善**[搜索插入位置](./Easy/search-insert-position/)
    - 直接插入排序c
- 2020年10月23日10:14:58 yujiecong更新[搜索插入位置](./Easy/search-insert-position/)
    - 直接插入排序python
- 2020年10月23日09:50:47 yujiecong更新[常见排序算法](./Sort-Algorithm)
    - 直接插入排序
        - C/C++
        - python
- 2020年10月22日19:21:43 yujiecong更新[实现 strStr](./Easy/implement-strstr/)
    - 滑动窗口
    - 最快查找
    - 双指针
- 2020年10月22日10:12:17 yujiecong更新[移除元素](./Easy/remove-element) 
    - 更改策略，主要以python为主，因为C太浪费时间了..
- 2020年10月22日00:09:56 yujiecong更新[删除排序数组中的重复项](./Easy/remove-duplicates-from-sorted-array)
    - 动态数组操作
        - 合并
        - 删除
    - 然后就去睡觉了
- 2020年10月21日11:26:12 yujiecong更新[合并两个有序链表](./Easy/merge-two-sorted-lists)
    - 解法2 使用动态插入
- 2020年10月20日12:11:43 yujiecong更新[合并两个有序链表](./Easy/merge-two-sorted-lists)
    - 解法1 是最蠢的全排方法(他的存在是为了考验链表的使用)
- 2020年10月19日18:30:08 yujiecong更新[有效的括号](./Easy/valid-parentheses)
    - 栈的典型应用
- 2020年10月18日17:18:21 yujiecong更新[用队列实现栈](./Easy/implement-stack-using-queues)
    - 有句话说的好，把栈指针反着指就是队列了
- 2020年10月18日00:52:40 yujiecong更新[最长公共前缀](./Easy/longest-common-prefix)
    - 知道滑动窗口
    - 利用木桶效应
    - 找到最优开局
- 2020年10月16日15:59:41 yujiecong更新[有序数组的平方](./Easy/squares-of-a-sorted-array)
    - 直接插入排序，以及常见排序
- 2020年10月15日21:37:04 yujiecong更新[罗马数字转整数](./Easy/roman-to-integer)
    - 手写罗马数字解析器
- 2020年10月13日21:35:39 yujiecong更新[回文数](./Easy/palindrome-number)
    - 双指针
    - 转化为字符串
    - 整数翻转
    - 防止溢出,特殊情况,极端情况
- 2020年10月11日16:29:00 yujiecong更新[两数之和](./Easy/two-sum)
    - 哈希表(python字典或者C++的map)
- 2020年10月11日20:47:43 yujiecong更新[反转整数](./Easy/reverse-integer)
    - 防止溢出
    - 整数翻转
## 目录
### 简单题
1. [两数之和](./Easy/two-sum)
2. [反转整数](./Easy/reverse-integer)
3. [回文数](./Easy/palindrome-number)
4. [罗马数字转整数](./Easy/roman-to-integer)
5. [有序数组的平方](./Easy/squares-of-a-sorted-array)
6. [最长公共前缀](./Easy/longest-common-prefix)
7. [用队列实现栈](./Easy/implement-stack-using-queues)
8. [有效的括号](./Easy/valid-parentheses)
9. [合并两个有序链表](./Easy/merge-two-sorted-lists)
10. [删除排序数组中的重复项](./Easy/remove-duplicates-from-sorted-array)
11. [移除元素](./Easy/remove-element)
12. [实现 strStr](./Easy/implement-strstr/)
13. [搜索插入位置](./Easy/search-insert-position/)
14. [外观数列](./Easy/count-and-say/)
15. [Maximum Subarray](./Easy/maximum-subarray)
16. [length-of-last-word](Easy\length-of-last-word) 
17.  [plus-one](Easy\plus-one) 
18.  [add-binary](Easy\add-binary) 
19.  [sqrtx](Easy\sqrtx) 
20.   [climbing-stairs](Easy\climbing-stairs) 
21.  [remove-duplicates-from-sorted-list](Easy\remove-duplicates-from-sorted-list) 
22. [merge-sorted-array](Easy\merge-sorted-array) 


### 中等题

1. 
### 困难题
1. 
## 背景
给自己加点料，建议大家多多提交issue和pr  

*注:yujiecong把自己的仓库移过来了,以后只在这里更新*   

> 话说搞robot算法肯定必不可少的，所以你们加油好吗？就算没有robot，就当开胃小菜吧，希望我们越来越好!

__这个仓库的目标是：__

1. 无聊的时候，能够来这里完善一下这里的内容
2. 提交issue并且引起讨论
3. 提升自己的思维能力，代码能力


## 维护者

[@yujiecong](https://github.com/yujiecong)。  

我在等你们的加入，那时候就会有你们了

## 如何贡献

非常欢迎你的加入！[提一个 Issue](https://github.com/ZHKU-Robot/Robot-algorithm-learning/issues/new) 或者提交一个 Pull Request。


本 Readme 遵循 [Contributor Covenant](http://contributor-covenant.org/version/1/3/0/) 行为规范。

## 贡献者

感谢以下参与项目的人：  
<a href="graphs/contributors"><img src="https://avatars2.githubusercontent.com/u/44287052?s=60&amp;v=4" /></a>

我在等你们的加入，那时候就会有你们的头像了
## 使用许可
[MIT License](./LICENSE)
