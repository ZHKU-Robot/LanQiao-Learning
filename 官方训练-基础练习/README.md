​			

# 没做出来的题目

-  [字母图形](#试题 基础练习 字母图形) 
-  [试题 基础练习 圆的面积](#试题 基础练习 圆的面积)
-  [2.17 N皇后问题](#2.17 N皇后问题)
-  [2.23 sin之舞](#2.23 sin之舞)
-  [2.25 完美的代价](#2.25 完美的代价)





## 试题 基础练习 数列排序

资源限制

时间限制：1.0s  内存限制：512.0MB

问题描述

　　给定一个长度为n的数列，将这个数列按从小到大的顺序排列。1<=n<=200

输入格式

　 第一行为一个整数n。
 　第二行包含n个整数，为待排序的数，每个整数的绝对值小于10000。

输出格式

　　输出一行，按从小到大的顺序输出排序后的数列。

样例输入

5
 8 3 6 4 9

样例输出

3 4 6 8 9

```python
input()
l=map(int,input().split())
for a in sorted(l):
    print(a,end=' ')
```



## 评测详情

| 提交序号 | 5500469                                                      |
| -------- | ------------------------------------------------------------ |
| 作者     | 余杰聪                                                       |
| 提交时间 | 02-20 20:18:37                                               |
| 评测结果 | 正确                                                         |
| 得分     | 100                                                          |
| CPU使用  | 31ms                                                         |
| 内存使用 | 7.957MB                                                      |
| 试题名称 | [基础练习 数列排序](http://lx.lanqiao.cn/problem.page?gpid=T52) |
| 语言     | PY                                                           |
| 源代码   |                                                              |
| 详细记录 | 评测点序号评测结果得分CPU使用内存使用下载评测数据1正确14.290ms7.902MB[输入](http://lx.lanqiao.cn/detail.page?submitid=5500469###) [输出](http://lx.lanqiao.cn/detail.page?submitid=5500469###) |







## 试题 基础练习 十六进制转八进制

 			

   		

资源限制

时间限制：1.0s  内存限制：512.0MB

**问题描述**
 　给定n个十六进制正整数，输出它们对应的八进制数。

 **输入格式**
 　输入的第一行为一个正整数n （1<=n<=10）。
 　接下来n行，每行一个由0~9、大写字母A~F组成的字符串，表示要转换的十六进制正整数，每个十六进制数长度不超过100000。

 **输出格式**
 　输出n行，每行为输入对应的八进制正整数。

 　**【注意**】
 　输入的十六进制数不会有前导0，比如012A。
 　输出的八进制数也不能有前导0。

 **样例输入**
 　2
 　39
 　123ABC

 **样例输出**
 　71
 　4435274

 　***\*【\**提示**】
 　先将十六进制数转换成某进制数，再由某进制数转换成八进制。

```
n=int(input())
for i in range(n):
    print(int(oct(int(input(),16))[2:]))
```



## 评测详情

| 提交序号 | 5500526                                                      |
| -------- | ------------------------------------------------------------ |
| 作者     | 余杰聪                                                       |
| 提交时间 | 02-20 20:25:39                                               |
| 评测结果 | 正确                                                         |
| 得分     | 100                                                          |
| CPU使用  | 437ms                                                        |
| 内存使用 | 8.214MB                                                      |
| 试题名称 | [基础练习 十六进制转八进制](http://lx.lanqiao.cn/problem.page?gpid=T51) |
| 语言     | PY                                                           |

## 试题 基础练习 十六进制转十进制



 			

   		

资源限制

时间限制：1.0s  内存限制：512.0MB

问题描述

　　从键盘输入一个不超过8位的正的十六进制数字符串，将它转换为正的十进制数后输出。
 　注：十六进制数中的10~15分别用大写的英文字母A、B、C、D、E、F表示。

样例输入

FFFF

样例输出

65535



```
print(int(input(),16))
```



## 评测详情

| 提交序号 | 5500545                                                      |
| -------- | ------------------------------------------------------------ |
| 作者     | 余杰聪                                                       |
| 提交时间 | 02-20 20:27:44                                               |
| 评测结果 | 正确                                                         |
| 得分     | 100                                                          |
| CPU使用  | 31ms                                                         |
| 内存使用 | 7.851MB                                                      |
| 试题名称 | [基础练习 十六进制转十进制](http://lx.lanqiao.cn/problem.page?gpid=T50) |
| 语言     | PY                                                           |



## 试题 基础练习 十进制转十六进制

 			

   		

资源限制

时间限制：1.0s  内存限制：512.0MB

问题描述

　　十六进制数是在程序设计时经常要使用到的一种整数的表示方式。它有0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F共16个符号，分别表示十进制数的0至15。十六进制的计数方法是满16进1，所以十进制数16在十六进制中是10，而十进制的17在十六进制中是11，以此类推，十进制的30在十六进制中是1E。
 　给出一个非负整数，将它表示成十六进制的形式。

输入格式

　　输入包含一个非负整数a，表示要转换的数。0<=a<=2147483647

输出格式

　　输出这个整数的16进制表示

样例输入

30

样例输出

1E



```
print(hex(int(input()))[2:].upper())
```



| 提交序号 | 5502595                                                      |
| -------- | ------------------------------------------------------------ |
| 作者     | 余杰聪                                                       |
| 提交时间 | 02-21 11:29:31                                               |
| 评测结果 | 正确                                                         |
| 得分     | 100                                                          |
| CPU使用  | 15ms                                                         |
| 内存使用 | 7.894MB                                                      |
| 试题名称 | [基础练习 十进制转十六进制](http://lx.lanqiao.cn/problem.page?gpid=T49) |
| 语言     | PY                                                           |



## 试题 基础练习 特殊回文数

 			

   		

资源限制

时间限制：1.0s  内存限制：512.0MB

问题描述

　　123321是一个非常特殊的数，它从左边读和从右边读是一样的。
 　输入一个正整数n， 编程求所有这样的五位和六位十进制数，满足各位数字之和等于n 。

输入格式

　　输入一行，包含一个正整数n。

输出格式

　　按从小到大的顺序输出满足条件的整数，每个整数占一行。

样例输入

52

样例输出

899998
 989989
 998899

数据规模和约定

　　1<=n<=54。

| 提交序号 | 5500781                                                      |
| -------- | ------------------------------------------------------------ |
| 作者     | 余杰聪                                                       |
| 提交时间 | 02-20 20:58:16                                               |
| 评测结果 | 正确                                                         |
| 得分     | 100                                                          |
| CPU使用  | 406ms                                                        |
| 内存使用 | 7.878MB                                                      |
| 试题名称 | [基础练习 特殊回文数](http://lx.lanqiao.cn/problem.page?gpid=T48) |
| 语言     | PY                                                           |

```
n=int(input())
r=[]
for i in range(10000,1000000):
    s=str(i)
    if s[::-1]==s:
        sum_=sum([int(a) for a in s])
        if sum_==n:
            print(i)

```



## 试题 基础练习 回文数

 			

   		

资源限制

时间限制：1.0s  内存限制：512.0MB

问题描述

　　1221是一个非常特殊的数，它从左边读和从右边读是一样的，编程求所有这样的四位十进制数。

输出格式

　　按从小到大的顺序输出满足条件的四位十进制数。



```
for i in range(1000,10000):
    if str(i)==str(i)[::-1]:
        print(i)
```

| 提交序号 | 5501619                                                      |
| -------- | ------------------------------------------------------------ |
| 作者     | 余杰聪                                                       |
| 提交时间 | 02-20 23:13:49                                               |
| 评测结果 | 正确                                                         |
| 得分     | 100                                                          |
| CPU使用  | 31ms                                                         |
| 内存使用 | 7.808MB                                                      |
| 试题名称 | [基础练习 回文数](http://lx.lanqiao.cn/problem.page?gpid=T47) |
| 语言     | PY                                                           |



## 试题 基础练习 特殊的数字



资源限制

时间限制：1.0s  内存限制：512.0MB

问题描述

　　153是一个非常特殊的数，它等于它的每位数字的立方和，即153=1*1*1+5*5*5+3*3*3。编程求所有满足这种条件的三位十进制数。

输出格式

　　按从小到大的顺序输出满足条件的三位十进制数，每个数占一行。



```
for i in range(100,1000):


    a=i%10
    b=i//10%10
    c=i//100

    if a**3+b**3+c**3==i:
        print(i)
```

| 提交序号 | 5501545                                                      |
| -------- | ------------------------------------------------------------ |
| 作者     | 余杰聪                                                       |
| 提交时间 | 02-20 22:55:32                                               |
| 评测结果 | 正确                                                         |
| 得分     | 100                                                          |
| CPU使用  | 0ms                                                          |
| 内存使用 | 7.851MB                                                      |
| 试题名称 | [基础练习 特殊的数字](http://lx.lanqiao.cn/problem.page?gpid=T46) |
| 语言     | PY                                                           |

## 试题 基础练习 杨辉三角形

 			

   		

资源限制

时间限制：1.0s  内存限制：256.0MB

 问题描述

杨辉三角形又称Pascal三角形，它的第i+1行是(a+b)i的展开式的系数。

它的一个重要性质是：三角形中的每个数字等于它两肩上的数字相加。

下面给出了杨辉三角形的前4行：

  1

 1 1

 1 2 1

1 3 3 1

给出n，输出它的前n行。

 输入格式

输入包含一个数n。

 输出格式

 输出杨辉三角形的前n行。每一行从这一行的第一个数开始依次输出，中间使用一个空格分隔。请不要在前面输出多余的空格。 

 样例输入

 4 

 样例输出

 1
 1 1
 1 2 1
 1 3 3 1 

 数据规模与约定

 1 <= n <= 34。 

```
rowList=[[1],[1,1]]
numRows=int(input())
for row in range(1, numRows - 1):
    templist = [1]
    lastrow = rowList[row]
    for colunm in range(1, len(lastrow)):
        templist.append(lastrow[colunm - 1] + lastrow[colunm])
    templist += [1]
    rowList.append(templist)
for l in rowList:
    for r in l:
        print(r,end=' ')
    print()
```



| 提交序号 | 5501572                                                      |
| -------- | ------------------------------------------------------------ |
| 作者     | 余杰聪                                                       |
| 提交时间 | 02-20 23:01:40                                               |
| 评测结果 | 正确                                                         |
| 得分     | 100                                                          |
| CPU使用  | 46ms                                                         |
| 内存使用 | 7.945MB                                                      |
| 试题名称 | [基础练习 杨辉三角形](http://lx.lanqiao.cn/problem.page?gpid=T10) |
| 语言     | PY                                                           |



## 试题 基础练习 查找整数

 			

   		

资源限制

时间限制：1.0s  内存限制：256.0MB

 问题描述

给出一个包含n个整数的数列，问整数a在数列中的第一次出现是第几个。

 输入格式

第一行包含一个整数n。

第二行包含n个非负整数，为给定的数列，数列中的每个数都不大于10000。

第三行包含一个整数a，为待查找的数。

 输出格式

 如果a在数列中出现了，输出它第一次出现的位置(位置从1开始编号)，否则输出-1。 

 样例输入

 6
 1 9 4 8 3 9
 9 

 样例输出

 2 

 数据规模与约定

 1 <= n <= 1000。 

| 提交序号 | 5501611                                                      |
| -------- | ------------------------------------------------------------ |
| 作者     | 余杰聪                                                       |
| 提交时间 | 02-20 23:12:02                                               |
| 评测结果 | 正确                                                         |
| 得分     | 100                                                          |
| CPU使用  | 31ms                                                         |
| 内存使用 | 7.886MB                                                      |
| 试题名称 | [基础练习 查找整数](http://lx.lanqiao.cn/problem.page?gpid=T9) |
| 语言     | PY                                                           |

```
input()
l=input().split()
find=input()
try:
    print(l.index(find)+1)
except ValueError:
    print(-1)
```





## 试题 基础练习 数列特征

 			

   		

资源限制

时间限制：1.0s  内存限制：256.0MB

问题描述

给出n个数，找出这n个数的最大值，最小值，和。

输入格式

第一行为整数n，表示数的个数。

第二行有n个数，为给定的n个数，每个数的绝对值都小于10000。

输出格式

输出三行，每行一个整数。第一行表示这些数中的最大值，第二行表示这些数中的最小值，第三行表示这些数的和。

样例输入

5
 1 3 -2 4 5

样例输出

5
 -2
 11

数据规模与约定

1 <= n <= 10000。

| 提交序号 | 5501601                                                      |
| -------- | ------------------------------------------------------------ |
| 作者     | 余杰聪                                                       |
| 提交时间 | 02-20 23:09:23                                               |
| 评测结果 | 正确                                                         |
| 得分     | 100                                                          |
| CPU使用  | 31ms                                                         |
| 内存使用 | 9.027MB                                                      |
| 试题名称 | [基础练习 数列特征](http://lx.lanqiao.cn/problem.page?gpid=T8) |
| 语言     | PY                                                           |

```
input()
l=[int(i) for i in input().split()]
print(max(l))
print(min(l))
print(sum(l))
```





## 试题 基础练习 字母图形

 			

资源限制

时间限制：1.0s  内存限制：256.0MB

问题描述

利用字母可以组成一些美丽的图形，下面给出了一个例子：

ABCDEFG

BABCDEF

CBABCDE

DCBABCD

EDCBABC

这是一个5行7列的图形，请找出这个图形的规律，并输出一个n行m列的图形。

输入格式

输入一行，包含两个整数n和m，分别表示你要输出的图形的行数的列数。

输出格式

输出n行，每个m个字符，为你的图形。

样例输入

5 7

样例输出

ABCDEFG
 BABCDEF
 CBABCDE
 DCBABCD
 EDCBABC

数据规模与约定

1 <= n, m <= 26。

## 

| 提交序号 | 5501694                                                      |
| -------- | ------------------------------------------------------------ |
| 作者     | 余杰聪                                                       |
| 提交时间 | 02-20 23:35:04                                               |
| 评测结果 | 错误                                                         |
| 得分     | 70                                                           |
| CPU使用  | 31ms                                                         |
| 内存使用 | 7.972MB                                                      |
| 试题名称 | [基础练习 字母图形](http://lx.lanqiao.cn/problem.page?gpid=T7) |
| 语言     | PY                                                           |

| 评测点序号 | 评测结果 | 得分  | CPU使用 | 内存使用 | 下载评测数据                                                 |
| ---------- | -------- | ----- | ------- | -------- | ------------------------------------------------------------ |
| 1          | 正确     | 10.00 | 0ms     | 7.875MB  | [输入](http://lx.lanqiao.cn/detail.page?submitid=5501694###) [输出](http://lx.lanqiao.cn/detail.page?submitid=5501694###) |
| 2          | 正确     | 10.00 | 0ms     | 7.933MB  | [VIP特权](http://lx.lanqiao.cn/help.page#vip)                |
| 3          | 错误     | 0.00  | 15ms    | 7.882MB  | [VIP特权](http://lx.lanqiao.cn/help.page#vip)                |
| 4          | 正确     | 10.00 | 15ms    | 7.937MB  | [VIP特权](http://lx.lanqiao.cn/help.page#vip)                |
| 5          | 错误     | 0.00  | 15ms    | 7.890MB  | [VIP特权](http://lx.lanqiao.cn/help.page#vip)                |
| 6          | 正确     | 10.00 | 31ms    | 7.945MB  | [VIP特权](http://lx.lanqiao.cn/help.page#vip)                |
| 7          | 正确     | 10.00 | 15ms    | 7.972MB  | [VIP特权](http://lx.lanqiao.cn/help.page#vip)                |
| 8          | 错误     | 0.00  | 31ms    | 7.886MB  | [VIP特权](http://lx.lanqiao.cn/help.page#vip)                |
| 9          | 正确     | 10.00 | 15ms    | 7.875MB  | [VIP特权](http://lx.lanqiao.cn/help.page#vip)                |
| 10         | 正确     | 10.00 | 31ms    | 7.929MB  | [VIP特权](http://lx.lanqiao.cn/help.page#vip)                |

这题有点问题，先mark一下





## 试题 基础练习 01字串

 			

   		

资源限制

时间限制：1.0s  内存限制：256.0MB

 问题描述

对于长度为5位的一个01串，每一位都可能是0或1，一共有32种可能。它们的前几个是：

00000

00001

00010

00011

00100

请按从小到大的顺序输出这32种01串。

 输入格式

 本试题没有输入。

 输出格式

 输出32行，按从小到大的顺序每行一个长度为5的01串。 

 样例输出

 00000
 00001
 00010
 00011
 <以下部分省略> 



刚好前几天学了递归的用法，其实是一个二叉树

## 评测详情

| 提交序号 | 5501760                                                      |
| -------- | ------------------------------------------------------------ |
| 作者     | 余杰聪                                                       |
| 提交时间 | 02-20 23:54:45                                               |
| 评测结果 | 正确                                                         |
| 得分     | 100                                                          |
| CPU使用  | 15ms                                                         |
| 内存使用 | 7.808MB                                                      |
| 试题名称 | [基础练习 01字串](http://lx.lanqiao.cn/problem.page?gpid=T6) |
| 语言     | PY                                                           |

```
def recursion(s):
    if len(s)==leng:
        l.append(s)
        return
    else:
        recursion(s+'0')
        recursion(s+'1')
l=[]

leng =5
recursion('')
for s in l:
    print(s)
```

另外还有一种用str.format的奇妙解法，我也是第一次知道

#### Python就是两行解决问题。。。

```
for i in range(32):
    print("{0:0>5}".format(format(i, 'b')))
```

> 上面这个引用自 https://blog.csdn.net/qq_31910669/article/details/103641497
>





## 试题 基础练习 闰年判断

 			

   		

资源限制

时间限制：1.0s  内存限制：256.0MB

 问题描述

给定一个年份，判断这一年是不是闰年。

当以下情况之一满足时，这一年是闰年：

\1. 年份是4的倍数而不是100的倍数；

\2. 年份是400的倍数。

其他的年份都不是闰年。

 输入格式

 输入包含一个整数y，表示当前的年份。

 输出格式

 输出一行，如果给定的年份是闰年，则输出yes，否则输出no。 

说明：当试题指定你输出一个字符串作为结果（比如本题的yes或者no，你需要严格按照试题中给定的大小写，写错大小写将不得分。 

 样例输入

 2013

 样例输出

 no

 样例输入

 2016

 样例输出

 yes

 数据规模与约定

 1990 <= y <= 2050。



## 评测详情

| 提交序号 | 5501759                                                      |
| -------- | ------------------------------------------------------------ |
| 作者     | 余杰聪                                                       |
| 提交时间 | 02-20 23:53:40                                               |
| 评测结果 | 正确                                                         |
| 得分     | 100                                                          |
| CPU使用  | 62ms                                                         |
| 内存使用 | 7.902MB                                                      |
| 试题名称 | [基础练习 闰年判断](http://lx.lanqiao.cn/problem.page?gpid=T5) |
| 语言     | PY                                                           |

```
year=int(input())
isleapYear='yes' if (year%4==0 and year%100!=0) or year%400==0 else 'no'
print(isleapYear)
```





## 试题 基础练习 Fibonacci数列

 			

   		

资源限制

时间限制：1.0s  内存限制：256.0MB

 问题描述

Fibonacci数列的递推公式为：Fn=Fn-1+Fn-2，其中F1=F2=1。

当n比较大时，Fn也非常大，现在我们想知道，Fn除以10007的余数是多少。

 输入格式

 输入包含一个整数n。

 输出格式

 输出一行，包含一个整数，表示Fn

说明：在本题中，答案是要求Fn除以10007的余数，因此我们只要能算出这个余数即可，而不需要先计算出Fn的准确值，再将计算的结果除以10007取余数，直接计算余数往往比先算出原数再取余简单。

 样例输入

 10

 样例输出

 55

 样例输入

 22

 样例输出

 7704

 数据规模与约定

 1 <= n <= 1,000,000。



如果用

```
def Fibonacci(n):
    if n<=2:
        return 1
    else:
        return (Fibonacci(n-1)+Fibonacci(n-2))%10007

print(Fibonacci(int(input())))
```

会这样


| 评测点序号 | 评测结果 | 得分  | CPU使用  | 内存使用 | 下载评测数据                                                 |
| ---------- | -------- | ----- | -------- | -------- | ------------------------------------------------------------ |
| 1          | 正确     | 10.00 | 15ms     | 7.878MB  | [输入](http://lx.lanqiao.cn/detail.page?submitid=5501765###) [输出](http://lx.lanqiao.cn/detail.page?submitid=5501765###) |
| 2          | 正确     | 10.00 | 0ms      | 7.871MB  | [VIP特权](http://lx.lanqiao.cn/help.page#vip)                |
| 3          | 正确     | 10.00 | 0ms      | 7.867MB  | [VIP特权](http://lx.lanqiao.cn/help.page#vip)                |
| 4          | 运行超时 | 0.00  | 运行超时 | 7.871MB  | [VIP特权](http://lx.lanqiao.cn/help.page#vip)                |
| 5          | 运行超时 | 0.00  | 运行超时 | 7.894MB  | [VIP特权](http://lx.lanqiao.cn/help.page#vip)                |
| 6          | 运行超时 | 0.00  | 运行超时 | 8.246MB  | [VIP特权](http://lx.lanqiao.cn/help.page#vip)                |
| 7          | 运行超时 | 0.00  | 运行超时 | 8.769MB  | [VIP特权](http://lx.lanqiao.cn/help.page#vip)                |
| 8          | 运行错误 | 0.00  | 15ms     | 8.867MB  | [VIP特权](http://lx.lanqiao.cn/help.page#vip)                |
| 9          | 运行错误 | 0.00  | 0ms      | 8.878MB  | [VIP特权](http://lx.lanqiao.cn/help.page#vip)                |
| 10         | 运行错误 | 0.00  | 0ms      | 8.875MB  | [VIP特权](http://lx.lanqiao.cn/help.page#vip)                |

所以我们要这样

```python
n = int(input())
l = [1, 1]
if n <= 2:
    print(1)
else:
    for _ in range(1, n - 2):
        l += [sum(l) % 10007]
        l.pop(0)
    print(sum(l)%10007)
```



| 提交序号 | 5501788                                                      |
| -------- | ------------------------------------------------------------ |
| 作者     | 余杰聪                                                       |
| 提交时间 | 02-21 00:06:18                                               |
| 评测结果 | 正确                                                         |
| 得分     | 100                                                          |
| CPU使用  | 359ms                                                        |
| 内存使用 | 7.898MB                                                      |
| 试题名称 | [基础练习 Fibonacci数列](http://lx.lanqiao.cn/problem.page?gpid=T4) |
| 语言     | PY                                                           |



## 试题 基础练习 圆的面积

 			

   		

资源限制

时间限制：1.0s  内存限制：256.0MB

 问题描述

 给定圆的半径r，求圆的面积。 

 输入格式

 输入包含一个整数r，表示圆的半径。 

 输出格式

 输出一行，包含一个实数，四舍五入保留小数点后7位，表示圆的面积。 

说明：在本题中，输入是一个整数，但是输出是一个实数。

对于实数输出的问题，请一定看清楚实数输出的要求，比如本题中要求保留小数点后7位，则你的程序必须**严格的**输出7位小数，输出过多或者过少的小数位数都是不行的，都会被认为错误。

实数输出的问题如果没有特别说明，舍入都是按四舍五入进行。

 样例输入

 4 

 样例输出

 50.2654825 

 数据规模与约定

 1 <= r <= 10000。 

 提示

 本题对精度要求较高，请注意π的值应该取较精确的值。你可以使用常量来表示π，比如PI=3.14159265358979323，也可以使用数学公式来求π，比如PI=atan(1.0)*4。 





| 提交序号 | 5502601                                                      |
| -------- | ------------------------------------------------------------ |
| 作者     | 余杰聪                                                       |
| 提交时间 | 02-21 11:31:01                                               |
| 评测结果 | 错误                                                         |
| 得分     | 90                                                           |
| CPU使用  | 15ms                                                         |
| 内存使用 | 7.921MB                                                      |
| 试题名称 | [基础练习 圆的面积](http://lx.lanqiao.cn/problem.page?gpid=T3) |
| 语言     | PY                                                           |
| 源代码   | 1`print(round(int(input())**2*3.14159265358979323,7))`       |





## 试题 基础练习 序列求和

 			

   		

资源限制

时间限制：1.0s  内存限制：256.0MB

 问题描述

 求1+2+3+...+n的值。 

 输入格式

 输入包括一个整数n。 

 输出格式

 输出一行，包括一个整数，表示1+2+3+...+n的值。 

 样例输入

 4 

 样例输出

 10 

 样例输入

 100 

说明：有一些试题会给出多组样例输入输出以帮助你更好的做题。

一般在提交之前所有这些样例都需要测试通过才行，但这不代表这几组样例数据都正确了你的程序就是完全正确的，潜在的错误可能仍然导致你的得分较低。

 样例输出

 5050 

 数据规模与约定

 1 <= n <= 1,000,000,000。 

说明：请注意这里的数据规模。

本题直接的想法是直接使用一个循环来累加，然而，当数据规模很大时，这种“暴力”的方法往往会导致超时。此时你需要想想其他方法。你可以试一试，如果使用1000000000作为你的程序的输入，你的程序是不是能在规定的上面规定的时限内运行出来。

本题另一个要值得注意的地方是答案的大小不在你的语言默认的整型(int)范围内，如果使用整型来保存结果，会导致结果错误。

如果你使用C++或C语言而且准备使用printf输出结果，则你的格式字符串应该写成%I64d以输出long long类型的整数。



| 提交序号 | 5502639                                                      |
| -------- | ------------------------------------------------------------ |
| 作者     | 余杰聪                                                       |
| 提交时间 | 02-21 11:38:33                                               |
| 评测结果 | 正确                                                         |
| 得分     | 100                                                          |
| CPU使用  | 15ms                                                         |
| 内存使用 | 7.890MB                                                      |
| 试题名称 | [基础练习 序列求和](http://lx.lanqiao.cn/problem.page?gpid=T2) |
| 语言     | PY                                                           |

```

n=int(input())

print(n+n*(n-1)//2)
```







## 试题 基础练习 A+B问题

 			

   		

资源限制

时间限制：1.0s  内存限制：256.0MB

问题描述

输入A、B，输出A+B。 

说明：在“问题描述”这部分，会给出试题的意思，以及所要求的目标。

输入格式

输入的第一行包括两个整数，由空格分隔，分别表示A、B。 

说明：“输入格式”是描述在测试你的程序时，所给的输入一定满足的格式。

做题时你应该假设所给的输入是一定满足输入格式的要求的，所以你不需要对输入的格式进行检查。多余的格式检查可能会适得其反，使用你的程序错误。

在测试的时候，系统会自动将输入数据输入到你的程序中，你不能给任何提示。比如，你在输入的时候提示“请输入A、B”之类的话是不需要的，这些多余的输出会使得你的程序被判定为错误。

输出格式

输出一行，包括一个整数，表示A+B的值。 

说明：“输出格式”是要求你的程序在输出结果的时候必须满足的格式。

在输出时，你的程序必须满足这个格式的要求，不能少任何内容，也不能多任何内容。如果你的内容和输出格式要求的不一样，你的程序会被判断为错误，包括你输出了提示信息、中间调试信息、计时或者统计的信息等。

样例输入

12 45 

说明：“样例输入”给出了一组满足“输入格式”要求的输入的例子。

这里给出的输入只是可能用来测试你的程序的一个输入，在测试的时候，还会有更多的输入用来测试你的程序。

样例输出

57 

说明：“样例输出”给出了一组满足“输出格式”要求的输出的例子。

样例输出中的结果是和样例输入中的是对应的，因此，你可以使用样例的输入输出简单的检查你的程序。

要特别指出的是，能够通过样例输入输出的程序并不一定是正确的程序，在测试的时候，会用很多组数据进行测试，而不局限于样例数据。有可能一个程序通过了样例数据，但测试的时候仍只能得0分，可能因为这个程序只在一些类似样例的特例中正确，而不具有通用性，再测试更多数据时会出现错误。

比如，对于本题，如果你写一个程序不管输入是什么都输入57，则样例数据是对的，但是测试其他数据，哪怕输入是1和2，这个程序也输出57，则对于其他数据这个程序都不正确。

数据规模与约定

-10000 <= A, B <= 10000。 

说明：“数据规模与约定”中给出了试题中主要参数的范围。

这个范围对于解题非常重要，不同的数据范围会导致试题需要使用不同的解法来解决。比如本题中给的A、B范围不大，可以使用整型(int)来保存，如果范围更大，超过int的范围，则要考虑其他方法来保存大数。

有一些范围在方便的时候是在“问题描述”中直接给的，所以在做题时不仅要看这个范围，还要注意问题描述。

提示

本题的C++源代码如下：

1. \#include <iostream>
2.  
3. using namespace std;
4.  
5. int main()
6. {
7.   int a, b;
8.   cin >> a >> b;
9.   cout << a + b;
10.   return 0;
11. }

本题的C源代码如下：

1. \#include <stdio.h>
2.  
3. int main()
4. {
5.   int a, b;
6.   scanf("%d%d", &a, &b);
7.   printf("%d", a+b);
8.   return 0;
9. }

本题的Java源代码如下：

1. import java.util.*;
2.  
3. public class Main
4. {
5.   public static void main(String args[])
6.   {
7. ​    Scanner sc = new Scanner(System.in);
8. ​    Integer a = sc.nextInt();
9. ​    Integer b = sc.nextInt();
10. ​    System.out.println(a + b);
11.   }
12. }

说明：要答题，请点击页面上方的“提交此题”按钮，页面将跳转到提交代码的页面，选择好你的编译语言，将你的编写好的代码粘贴到代码框中，再点击“提交答案”即可。

你的答案提交给系统后系统会自动对你的代码进行判分，并跳转到结果的列表里面，你可以直接从列表中看到你提交的代码的状态，一般几秒钟后就可以看到判分的结果。

本题作为第一题，在提示中已经分别给了C++和Java的代码，你可以直接把这个代码拷贝过去作为自己的代码提交。

请特别注意，Java的主类名必须是Main。



| 提交序号 | 5502653                                                      |
| -------- | ------------------------------------------------------------ |
| 作者     | 余杰聪                                                       |
| 提交时间 | 02-21 11:40:55                                               |
| 评测结果 | 正确                                                         |
| 得分     | 100                                                          |
| CPU使用  | 31ms                                                         |
| 内存使用 | 7.906MB                                                      |
| 试题名称 | [基础练习 A+B问题](http://lx.lanqiao.cn/problem.page?gpid=T1) |
| 语言     | PY                                                           |

```
print(sum(map(int,input().split())))
```



以下的题需要vip  然而 我没有，所以你懂的

## 2.14 阶乘计算

问题描述
 　　输入一个正整数n，输出n!的值。
 　　其中n!=1*2*3*…*n。
 算法描述
 　　n!可能很大，而计算机能表示的整数范围有限，需要使用高精度计算的方法。使用一个数组A来表示一个大整数a，A[0]表示a的个位，A[1]表示a的十位，依次类推。
 　　将a乘以一个整数k变为将数组A的每一个元素都乘以k，请注意处理相应的进位。
 　　首先将a设为1，然后乘2，乘3，当乘到n时，即得到了n!的值。
 输入格式
 　　输入包含一个正整数n，n<=1000。
 输出格式
 　　输出n!的准确值。
 样例输入
 10
 样例输出
 3628800
 **特别注意n的规模**
 首先用递归只能解决1到几百以内的阶乘

```
s=1
for i in range(1,int(input())+1):
    s*=i
print(s)
```



## 2.15 长整数加法

问题描述
 　　输入两个整数a和b，输出这两个整数的和。a和b都不超过100位。
 算法描述
 　　由于a和b都比较大，所以不能直接使用语言中的标准数据类型来存储。对于这种问题，一般使用数组来处理。
 　　定义一个数组A，A[0]用于存储a的个位，A[1]用于存储a的十位，依此类推。同样可以用一个数组B来存储b。
 　　计算c = a +  b的时候，首先将A[0]与B[0]相加，如果有进位产生，则把进位（即和的十位数）存入r，把和的个位数存入C[0]，即C[0]等于(A[0]+B[0])%10。然后计算A[1]与B[1]相加，这时还应将低位进上来的值r也加起来，即C[1]应该是A[1]、B[1]和r三个数的和．如果又有进位产生，则仍可将新的进位存入到r中，和的个位存到C[1]中。依此类推，即可求出C的所有位。
 　　最后将C输出即可。
 输入格式
 　　输入包括两行，第一行为一个非负整数a，第二行为一个非负整数b。两个整数都不超过100位，两数的最高位都不是0。
 输出格式
 　　输出一行，表示a + b的值。
 样例输入
 20100122201001221234567890
 2010012220100122
 样例输出
 20100122203011233454668012

这是自己的答案，没有验证过，可能是错的

```
a = input()
b = input()
c = ""
r = 0
m = max([len(a), len(b)])
t=''.join(['0' for _ in range(abs(len(a)-len(b)))])


if len(a)>len(b):
    b=t+b
else:
    a=t+a

for i in range(- 1, -m-1, -1):
    s = sum(map(int, [a[i], b[i]]))
    c =str((s + r)%10)+c
    if s+r >= 10:
        # 产生一个进位
        r =(r+s)//10
    else:
        r = 0
    #当前位
    # print("当前和",s)
    # print("当前位",c)
    # print("进位",r)

c=str(r if r!=0 else '')+c
print((a if len(a)>len(b) else b)[:abs(len(a)-len(b))]+c)
```





## 2.16 哈夫曼树

问题描述
 　　Huffman树在编码中有着广泛的应用。在这里，我们只关心Huffman树的构造过程。
 　　给出一列数{pi}={p0, p1, …, pn-1}，用这列数构造Huffman树的过程如下：
 　　1. 找到{pi}中最小的两个数，设为pa和pb，将pa和pb从{pi}中删除掉，然后将它们的和加入到{pi}中。这个过程的费用记为pa + pb。
 　　2. 重复步骤1，直到{pi}中只剩下一个数。
 　　在上面的操作过程中，把所有的费用相加，就得到了构造Huffman树的总费用。
 　　本题任务：对于给定的一个数列，现在请你求出用该数列构造Huffman树的总费用。

例如，对于数列{pi}={5, 3, 8, 2, 9}，Huffman树的构造过程如下：
 　　1. 找到{5, 3, 8, 2, 9}中最小的两个数，分别是2和3，从{pi}中删除它们并将和5加入，得到{5, 8, 9, 5}，费用为5。



    　　1. 找到{5, 8, 9, 5}中最小的两个数，分别是5和5，从{pi}中删除它们并将和10加入，得到{8, 9, 10}，费用为10。
    　　2. 找到{8, 9, 10}中最小的两个数，分别是8和9，从{pi}中删除它们并将和17加入，得到{10, 17}，费用为17。
    　　3. 找到{10, 17}中最小的两个数，分别是10和17，从{pi}中删除它们并将和27加入，得到{27}，费用为27。
    　　4. 现在，数列中只剩下一个数27，构造过程结束，总费用为5+10+17+27=59。
       输入格式
        　　输入的第一行包含一个正整数n（n<=100）。
        　　接下来是n个正整数，表示p0, p1, …, pn-1，每个数不超过1000。
        输出格式
        　　输出用这些数构造Huffman树的总费用。
        样例输入
        5
        5 3 8 2 9
        样例输出
        59



哈弗曼我们很熟了，哈哈哈

很容易的

​	

```
n=input()
l=list(map(int,input().split()))
s=0
for i in range(int(n)-1):
    m1=min(l)
    l.pop(l.index(m1))
    m2=min(l)
    l[l.index(m2)]=m1+m2
    s+=m1+m2
print(s)
```



## 2.17 N皇后问题

要在n*n的国际象棋棋盘中放n个皇后，使任意两个皇后都不能互相吃掉。规则：皇后能吃掉同一行、同一列、同一对角线的任意棋子。求所有的解。n=8是就是著名的八皇后问题了。



不看解析做不出，可以去https://leetcode-cn.com/problems/n-queens/submissions/看看



## 2.18 报时助手

问题描述
 　　给定当前的时间，请用英文的读法将它读出来。
 　　时间用时h和分m表示，在英文的读法中，读一个时间的方法是：
 　　如果m为0，则将时读出来，然后加上“o’clock”，如3:00读作“three o’clock”。
 　　如果m不为0，则将时读出来，然后将分读出来，如5:30读作“five thirty”。	
 　　时和分的读法使用的是英文数字的读法，其中0~20读作：
 　　0:zero, 1: one, 2:two, 3:three, 4:four, 5:five, 6:six, 7:seven,  8:eight, 9:nine, 10:ten, 11:eleven, 12:twelve, 13:thirteen, 14:fourteen, 15:fifteen, 16:sixteen, 17:seventeen, 18:eighteen, 19:nineteen,  20:twenty。
 　　30读作thirty，40读作forty，50读作fifty。
 　　对于大于20小于60的数字，首先读整十的数，然后再加上个位数。如31首先读30再加1的读法，读作“thirty one”。
 　　按上面的规则21:54读作“twenty one fifty four”，9:07读作“nine seven”，0:15读作“zero fifteen”。
 输入格式
 　　输入包含两个非负整数h和m，表示时间的时和分。非零的数字前没有前导0。h小于24，m小于60。
 输出格式
 　　输出时间时刻的英文。
 样例输入
 0 15
 样例输出
 zero fifteen



穷举字典爆破即可

```
h, m = map(int, input().split())

d = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
     10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
     17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 21: 'twenty one', 22: 'twenty two',
     23: 'twenty three', 30: 'thirty', 40: 'forty', 50: 'fifty'}


if m == 0:
    print(d[h] + ' o\'clock')
else:
    print(d[h], end=' ')
    if 0 < m <= 20 or m == 30 or m == 40 or m == 50:
        print(d[m])
    elif 20 < m < 30:
        print(d[20] + ' ' + d[m - 20])
    elif 30 < m < 40:
        print(d[30] + ' ' + d[m - 30])
    elif 40 < m < 50:
        print(d[40] + ' ' + d[m - 40])
    else:
        print(d[50] + ' ' + d[m - 50])
```



## 2.19 回形取数

问题描述
 　　回形取数就是沿矩阵的边取数，若当前方向上无数可取或已经取过，则左转90度。一开始位于矩阵左上角，方向向下。
 输入格式
 　　输入第一行是两个不超过200的正整数m, n，表示矩阵的行和列。接下来m行每行n个整数，表示这个矩阵。
 输出格式
 　　输出只有一行，共mn个数，为输入矩阵回形取数得到的结果。数之间用一个空格分隔，行末不要有多余的空格。
 样例输入
 3 3
 1 2 3
 4 5 6
 7 8 9
 样例输出
 1 4 7 8 9 6 3 2 5
 样例输入
 3 2
 1 2
 3 4
 5 6
 样例输出
 1 3 5 6 4 2

obviously，一道找规律的题，如果有草稿纸画一下会好做很多

```
m, n=map(int, input().split())
l=[]
for r in range(m):
    l.append([int(i) for i in input().split()])

# 一开始 的方向是向下
down,up,right,left=1,2,3,4

_row=0
_col=0
for r in range(n//2+1):
    print("round",r)
    for c in range(_row,m-_row):
        if l[c][r]!=-1:
            print(l[c][r],end=' ')

            l[c][r]=-1
        _row += 1
    _row-=1
    _col+=1

    for c in range(_col,n-_col+1):
        if l[_row][_col]!=-1:
            print(l[_row][_col],end=' ')
            l[_row][_col]=-1
        _col += 1
    _col-=1
    _row-=1

    for c in range(_row,r-1,-1):
        if l[c][_col]!=-1:
            print(l[c][_col],end=' ')
            l[c][_col]=-1
        _row -= 1
    _row+=1
    _col-=1

    for c in range(_col,r,-1):
        if l[_row][c]!=-1:
            print(l[_row][c],end=' ')
            l[_row][c]=-1
        _col-=1
    _col+=1
    _row+=1
    print()
```



实话实说，很讨厌这种题，这里很可能是错的，不过有啥所谓呢？



## 2.20 龟兔赛跑预测

问题描述
  　话说这个世界上有各种各样的兔子和乌龟，但是研究发现，所有的兔子和乌龟都有一个共同的特点——喜欢赛跑。于是世界上各个角落都不断在发生着乌龟和兔子的比赛，小华对此很感兴趣，于是决定研究不同兔子和乌龟的赛跑。他发现，兔子虽然跑比乌龟快，但它们有众所周知的毛病——骄傲且懒惰，于是在与乌龟的比赛中，一旦任一秒结束后兔子发现自己领先t米或以上，它们就会停下来休息s秒。对于不同的兔子，t，s的数值是不同的，但是所有的乌龟却是一致——它们不到终点决不停止。
  　然而有些比赛相当漫长，全程观看会耗费大量时间，而小华发现只要在每场比赛开始后记录下兔子和乌龟的数据——兔子的速度v1（表示每秒兔子能跑v1米），乌龟的速度v2，以及兔子对应的t，s值，以及赛道的长度l——就能预测出比赛的结果。但是小华很懒，不想通过手工计算推测出比赛的结果，于是他找到了你——清华大学计算机系的高才生——请求帮助，请你写一个程序，对于输入的一场比赛的数据v1，v2，t，s，l，预测该场比赛的结果。
 输入格式
 　　输入只有一行，包含用空格隔开的五个正整数 ，其中(v1,v2<=100;t<=300;s<=10;l<=10000且为v1,v2的公倍数)
 输出格式
 　　输出包含两行，第一行输出比赛结果——一个大写字母“T”或“R”或“D”，分别表示乌龟获胜，兔子获胜，或者两者同时到达终点。
 　　第二行输出一个正整数，表示获胜者（或者双方同时）到达终点所耗费的时间（秒数）。
 样例输入
 10 5 5 2 20
 样例输出
 D
 4
 样例输入
 10 5 5 1 20
 样例输出
 R
 3
 样例输入
 10 5 5 3 20
 样例输出
 T
 4

```
v1,v2,t,s,l=map(int,input().split())

rabbitDistance=0
turtleDistance=0

_break=0
count=0
rest=False
while rabbitDistance<l and turtleDistance<l:
    if rabbitDistance-turtleDistance>=5:
        # 开始休息
        rest=True
    if not rest:
        rabbitDistance += v1
    else:
        _break+=1
    if _break==s:
        rest=False
        _break=0

    turtleDistance+=v2
    count+=1

    print(rabbitDistance,turtleDistance)

if rabbitDistance<turtleDistance:
    print('T')
elif rabbitDistance>turtleDistance:
    print('R')
else:
    print('D')

print(count)
```

这种题就很简单了，不用说了



## 2.21 芯片测试

问题描述
 　　有n（2≤n≤20）块芯片，有好有坏，已知好芯片比坏芯片多。
 　　每个芯片都能用来测试其他芯片。用好芯片测试其他芯片时，能正确给出被测试芯片是好还是坏。而用坏芯片测试其他芯片时，会随机给出好或是坏的测试结果（即此结果与被测试芯片实际的好坏无关）。
 　　给出所有芯片的测试结果，问哪些芯片是好芯片。
 输入格式
 　　输入数据第一行为一个整数n，表示芯片个数。
 　　第二行到第n+1行为n*n的一张表，每行n个数据。表中的每个数据为0或1，在这n行中的第i行第j列（1≤i,  j≤n）的数据表示用第i块芯片测试第j块芯片时得到的测试结果，1表示好，0表示坏，i=j时一律为1（并不表示该芯片对本身的测试结果。芯片不能对本身进行测试）。
 输出格式
 　　按从小到大的顺序输出所有好芯片的编号
 样例输入
 3
 1 0 1
 0 1 0
 1 0 1
 样例输出
 1 3
 **解题思路：**

>  **重点是好芯片比坏芯片多**
>  如果忽略这个问题就很难解决，本人开始你就不幸忽略了。。。
>  既然好芯片比坏芯片多，那么我们只需记录每一列0的个数就行了，若个数超过n/2，则此芯片为坏芯片
>  一个chip列表来记录芯片的好坏



```
n = int(input())

arr = [[] for _ in range(n)]

chip = [True for _ in range(n)]

for i in range(n):
    arr_ = input().split()
    for j in range(n):
        arr[i].append(int(arr_[j]))

for i in range(n):
    count = 0
    for j in range(n):
        if arr[j][i] == 0:
            count += 1
    if count > n / 2:
        chip[i] = False

for i in range(n):
    if chip[i]:
        print(i + 1, end=' ')

```





## 2.22 FJ字符串

问题描述
 　　FJ在沙盘上写了这样一些字符串：
 　　A1 = “A”
 　　A2 = “ABA”
 　　A3 = “ABACABA”
 　　A4 = “ABACABADABACABA”
 　　… …
 　　你能找出其中的规律并写所有的数列AN吗？
 输入格式
 　　仅有一个数：N ≤ 26。
 输出格式
 　　请输出相应的字符串AN，以一个换行符结束。输出中不得含有多余的空格或换行、回车符。
 样例输入
 3
 样例输出
 ABACABA



找规律的题

规律比较容易看出来的

```
letters=[chr(i) for i in range(ord('A'),ord('Z')+1)]
# print(letters)
result=''
for i in range(int(input())):
    result=result+letters[i]+result
print(result)

```



## 2.23 sin之舞

问题描述
 　　最近FJ为他的奶牛们开设了数学分析课，FJ知道若要学好这门课，必须有一个好的三角函数基本功。所以他准备和奶牛们做一个“Sine之舞”的游戏，寓教于乐，提高奶牛们的计算能力。
 　　不妨设
 　　An=sin(1–sin(2+sin(3–sin(4+…sin(n))…)
 　　Sn=(…(A1+n)A2+n-1)A3+…+2)An+1
 　　FJ想让奶牛们计算Sn的值，请你帮助FJ打印出Sn的完整表达式，以方便奶牛们做题。
 输入格式
 　　仅有一个数：N<201。
 输出格式
 　　请输出相应的表达式Sn，以一个换行符结束。输出中不得含有多余的空格或换行、回车符。
 样例输入
 3
 样例输出
 ((sin(1)+3)sin(1–sin(2))+2)sin(1–sin(2+sin(3)))+1


真的烦死了

递归不出来

```
N=int(input())
An=str(N)
Sn=''
def getAn(n,a):
    if n<0:
        return a
    return getAn(n - 1,'{}{}sin({})'.format(n,'+' if n %2==0 else '-',a))


def getSn(n,sn):
    if n>N:
        return sn
    # print(sn)N-n+1
    an=getAn(n,str(n))[2:]
    print(an)
    return getSn(n + 1,'({}){}+{}'.format(sn,an,n))

# getAn(N)
print(getSn(1,''))
```

就做到这里，傻逼题，气死我了



> 答案在这里
>
> https://blog.csdn.net/qq_31910669/article/details/103641497



```
def A(n, k):

    if n == k:
        return

    print('sin(%d' % (n + 1), end='')

    if n + 1 != k:  # 若后边还有式子，判断是输出+号还是-号
        if n % 2 == 1:
            print('+', end='')
        else:
            print('-', end='')
    else:  # 若后边没有式子，输出右括号结束
        # 注意，这里只输出最后一次的右括号，前边左括号对应的右括号在S()函数中补全
        print(')', end='')

    n += 1

    A(n, k)  # 递归调用自身


def S(n):

    k = t = 1

    if n == 0:
        return

    for i in range(n - 1):
        print('(', end='')

    while n != 0:
        A(0, k)
        for i in range(t - 1):  # 不全A()函数中的括号
            print(')', end='')
        print('+%d' % n, end='')
        if n != 1:  # 最后一项加完整数之和不必再输出右括号
            print(')', end='')
        k += 1
        t += 1
        n -= 1


n = int(input())

# A(0, 3)

S(n)


```





## 2.24 数的读法

问题描述
 　　Tom教授正在给研究生讲授一门关于基因的课程，有一件事情让他颇为头疼：一条染色体上有成千上万个碱基对，它们从0开始编号，到几百万，几千万，甚至上亿。
 　　比如说，在对学生讲解第1234567009号位置上的碱基时，光看着数字是很难准确的念出来的。
 　　所以，他迫切地需要一个系统，然后当他输入12 3456 7009时，会给出相应的念法：
 　　十二亿三千四百五十六万七千零九
 　　用汉语拼音表示为
 　　shi er yi san qian si bai wu shi liu wan qi qian ling jiu
 　　这样他只需要照着念就可以了。
 　　你的任务是帮他设计这样一个系统：给定一个阿拉伯数字串，你帮他按照中文读写的规范转为汉语拼音字串，相邻的两个音节用一个空格符格开。
 　　注意必须严格按照规范，比如说“10010”读作“yi wan ling yi shi”而不是“yi wan ling  shi”，“100000”读作“shi wan”而不是“yi shi wan”，“2000”读作“er qian”而不是“liang  qian”。
 输入格式
 　　有一个数字串，数值大小不超过2,000,000,000。
 输出格式
 　　是一个由小写英文字母，逗号和空格组成的字符串，表示该数的英文读法。
 样例输入
 1234567009
 样例输出
 shi er yi san qian si bai wu shi liu wan qi qian ling jiu



这种题快速过，因为没意思

而且如果没有测试，复杂情况很多，实话实说不想做

直接来看题解吧



```
n = input()

num2pinyin = {'0': 'ling', '1': 'yi', '2': 'er', '3': 'san', '4': 'si', '5': 'wu',
           '6': 'liu', '7': 'qi', '8': 'ba', '9': 'jiu'}
unit2pinyin = {0: '', 1: '', 2: 'shi', 3: 'bai', 4: 'qian', 5: 'wan', 6: 'shi',
               7: 'bai', 8: 'qian', 9: 'yi', 10: 'shi'}
n = n + ' '

l = len(n) - 1

for i in range(l):
    j = int(n[i])
    if j != 0:  # 不为0时的读法
        if (l - i == 2 or l - i == 6 or l - i == 10) and j == 1:
            # 在十位，十万位，十亿位置且位于开头的1不读
            # 例子：
            # 1111111111 会读出 yi shi yi yi yi qian yi bai yi shi yi wan yi qian yi bai yi shi yi
            # 111111 会读出 yi shi yi wan yi qian yi bai yi shi yi
            # 11 会读出 yi shi yi
            # 加上此约束后，则不会读出开头的 yi
            if i != 0:  # 第一个1不输出1， 若不添加此条件，12会读出 yi shi er
                print(num2pinyin['1'], end=' ')
            print(unit2pinyin[2], end=' ')
            continue
        print(num2pinyin[n[i]], end=' ')
        print(unit2pinyin[l - i], end=' ')
    else:  # 处理0的读法问题
        if l - i == 5 or l - i == 9:  # 如果此0是在万位或亿位，则读出万或亿
            print(unit2pinyin[l - i], end=' ')
        if n[i + 1] == '0' or i == l - 1:  # 如果后一位仍然为0，或者，当前是最后以为，则不读此0
            continue
        print(num2pinyin['0'], end=' ')  # 否则才读出这个零
```







## 2.25 完美的代价

问题描述
 　　回文串，是一种特殊的字符串，它从左往右读和从右往左读是一样的。小龙龙认为回文串才是完美的。现在给你一个串，它不一定是回文的，请你计算最少的交换次数使得该串变成一个完美的回文串。
 　　交换的定义是：交换两个相邻的字符
 　　例如mamad
 　　第一次交换 ad : mamda
 　　第二次交换 md : madma
 　　第三次交换 ma : madam (回文！完美！)
 输入格式
 　　第一行是一个整数N，表示接下来的字符串的长度(N <= 8000)
 　　第二行是一个字符串，长度为N.只包含小写字母
 输出格式
 　　如果可能，输出最少的交换次数。
 　　否则输出Impossible
 样例输入
 5
 mamad
 样例输出
 3

这题有些难。。。看了解析才看懂



```
input()
s=input()
n=len(s)
l=list(s)
c=f=0
m=len(l)
for i in range(m-1):
    for j in range(m-1,i-1,-1 ):
        print(i,j)
        if i==j:
            if n%2==0 or f==1:
                print("Impossible")
                exit()
            flag=1
            c+=n//2-i
        elif l[j]==l[i]: #如果找到相同字母，就要移动到相应位置
            #懂了
            for k in range(j,m-1):
                print("{} swap {}".format(l[k],l[k+1]))
                l[k],l[k+1]=l[k+1],l[k]
                print("s={}".format(''.join(l)))
                c+=1
            m-=1 #倒退一格，因为当前位置已经好了
            break
print(c)
```





还是看下一题吧

## 2.26 矩形面积交

问题描述
 　　平面上有两个矩形，它们的边平行于直角坐标系的X轴或Y轴。对于每个矩形，我们给出它的一对相对顶点的坐标，请你编程算出两个矩形的交的面积。
 输入格式
 　　输入仅包含两行，每行描述一个矩形。
 　　在每行中，给出矩形的一对相对顶点的坐标，每个点的坐标都用两个绝对值不超过10^7的实数表示。
 输出格式
 　　输出仅包含一个实数，为交的面积，保留到小数后两位。
 样例输入
 1 1 3 3
 2 2 4 4
 样例输出
 1.00



![1614231593299](img/1614231593299.png)

我们只需要找到一个矩阵1的右下角坐标和 矩阵2 的左上角坐标，做判断就行



注意python 保留小数点的方式 用 '%.2f'是最好的，也是c/c++喜欢用的方式

round这个呢就是四舍五入用的，不能直接用来添加0

```

rect_1 = list(map(float, input().split()))

rect_2 = list(map(float, input().split()))
area = 0

x1 = max(min(rect_1[0], rect_1[2]), min(rect_2[0], rect_2[2]))

y1 = max(min(rect_1[1], rect_1[3]), min(rect_2[1], rect_2[3]))

x2 = min(max(rect_1[0], rect_1[2]), max(rect_2[0], rect_2[2]))

y2 = min(max(rect_1[1], rect_1[3]), max(rect_2[1], rect_2[3]))

if x1 < x2 and y1 < y2:
    area = (x2 - x1) * (y2 - y1)
    print('%.2f' % area)
else:
    print('%.2f' % area)
```





## 2.27 矩阵乘法

问题描述
 　　给定一个N阶矩阵A，输出A的M次幂（M是非负整数）
 　　例如：
 　　A =
 　　1 2
 　　3 4
 　　A的2次幂
 　　7 10
 　　15 22
 输入格式
 　　第一行是一个正整数N、M（1<=N<=30, 0<=M<=5），表示矩阵A的阶数和要求的幂数
 　　接下来N行，每行N个绝对值不超过10的非负整数，描述矩阵A的值
 输出格式
 　　输出共N行，每行N个整数，表示A的M次幂所对应的矩阵。相邻的数之间用一个空格隔开
 样例输入
 2 2
 1 2
 3 4
 样例输出
 7 10
 15 22



我先去别的，我已经开始感觉很难了