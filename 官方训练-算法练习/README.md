## 试题 算法训练 网络流裸题

 			

   		

资源限制

时间限制：1.0s  内存限制：256.0MB

问题描述

　　一个有向图，求1到N的最大流

输入格式

　　第一行N M，表示点数与边数
 　接下来M行每行s t c表示一条从s到t的容量为c的边

输出格式

　　一个数最大流量

样例输入

6 10
 1 2 4
 1 3 8
 2 3 4
 2 4 4
 2 5 1
 3 4 2
 3 5 2
 4 6 7
 5 4 6
 5 6 3

样例输出

8

 数据约定：
 n<=1000 m<=10000





## 试题 算法训练 猴子吃包子

 			

   		

资源限制

时间限制：1.0s  内存限制：256.0MB

问题描述

　　从前，有一只吃包子很厉害的猴子，它可以吃无数个包子，但是，它吃不同的包子速度也不同；肉包每秒钟吃x个；韭菜包每秒钟吃y个；没有馅的包子每秒钟吃z个；现在有x1个肉包，y1个韭菜包，z1个没有馅的包子；问：猴子吃完这些包子要多久？结果保留p位小数。

输入格式

　　输入1行，包含7个整数，分别表示吃不同包子的速度和不同包子的个数和保留的位数。

输出格式

　　输出一行，包含1个实数，表示吃完所有包子的时间。

样例输入

4 3 2 20 30 15 2

样例输出

22.50

数据规模和约定

　　0<x<100;0<y<100;0<z<100;0<x1<=1000000;0<y1<=10000000;0<z1<=10000000;0<p<=1000



过于送分

```
vx,vy,vz,x1,y1,z1,p=map(int,input().split())
print("%.2f"%(x1/vx+y1/vy+z1/vz))

```

## 评测详情

| 提交序号 | 5534747                                                      |
| -------- | ------------------------------------------------------------ |
| 作者     | 余杰聪                                                       |
| 提交时间 | 02-27 18:41:01                                               |
| 评测结果 | 正确                                                         |
| 得分     | 100                                                          |
| CPU使用  | 15ms                                                         |
| 内存使用 | 7.820MB                                                      |
| 试题名称 | [算法训练 猴子吃包子](http://lx.lanqiao.cn/problem.page?gpid=T632) |
| 语言     | PY                                                           |



## 试题 算法训练 Yaroslav and Algorithm

 			

资源限制

时间限制：100ms  内存限制：128.0MB

问题描述

　　（这道题的数据和SPJ已完工，尽情来虐吧！）

 　Yaroslav喜欢算法。我们将描述一个他最喜欢的算法。

 　1.这个算法接受一个字符串作为输入。我们设这个输入字符串为a。
 　2.这个算法由一些命令组成。i号命令的形式为"s[i]>>w[i]"或"s[i]<>w[i]"，其中s[i]和w[i]是长度不超过7的字符串（可以为空），由数字或字符"?"组成。
 　3.这个算法每次寻找一个编号最小的命令i，使得s[i]是a的子串。如果没有找到这样的命令，那么整个算法终止。
 　4.设找到的命令编号为k。在字符串a中，s[k]第一次出现的位置会被w[k]替换。如果这个命令形如"s[k]>>w[k]"，那么这个算法继续执行（译注：回到第3步）。否则，算法终止。
 　5.算法的输出就是算法终止时字符串a的值。

 　Yaroslav有一个n个正整数的集合，他需要一个这样的算法，且能够使每一个数加1。更正式地，如果我们把每个数看成一个十进制表示的字符串，那么对于每个字符串独立地运行这个算法，这个算法需要输出一个输入串对应的数+1的字符串。
 　帮帮他吧！

输入格式

　　第一行包含一个整数n（集合中数的个数），接下来n行，每行包含一个正整数。

输出格式

　　输出一个符合题意的算法（能够分别将每个数增加1）。第i行输出这个算法的第i个命令，不包含空格。
 　你的算法将会对于每个输入运行一遍。你的输出会被认为是正确的，当且仅当：
 　·每行都是一个合法的命令（格式见题目描述）
 　·命令的条数不能超过50。
 　·算法需要对每个给出的数+1。
 　·为了得到结果，算法必须对于每个输入都执行不超过200步。

样例输入

2
 10
 79

样例输出

10<>11
 79<>80

数据规模和约定

　　1≤每个数≤10^25。共有20个测试点，对于第i个测试点，n=5i。





题目太长不看



## 试题 算法训练 Sereja and Squares

 			

   		

资源限制

时间限制：4.0s  内存限制：256.0MB

问题描述

　　Sereja在平面上画了n个点，点i在坐标(i,0)。然后，Sereja给每个点标上了一个小写或大写英文字母。Sereja不喜欢字母"x"，所以他不用它标记点。Sereja认为这些点是漂亮的，当且仅当：
 　·所有的点可以被分成若干对，使得每个点恰好属于一一对之中。
 　·在每对点中，横坐标较小的会被标上小写字母，较大的会被标上对应的大写字母。
 　·如果我们在每对点上画一个正方形，其中已知的一对点会作为正方形的相对的顶点，它们间的线段会成为正方形的对角线，那么在所有画出的正方形中不会有相交或触碰的情况。
 　小Petya擦掉了一些小写字母和所有大写字母，现在Sereja想知道有多少种方法来还原每个点上的字母，使得还原后这些点是漂亮的。

输入格式

　　第一行是一个整数n，表示点的个数。
 　第二行是一个长度为n的字符串，包含小写字母和问号"?"，是按照横坐标递增的顺序的每个点的描述。问号表示这个点的字母被Petya擦掉了。保证输入串不含字母"x"。

输出格式

　　输出答案对4294967296取模的值。如果没有可行的方案，输出0。

样例输入

4
 a???

样例输出

50

样例输入

4
 abc?

样例输出

0

样例输入

6
 abc???

样例输出

1

数据规模和约定

　　20个测试点的n分别为：
 　5,10,20,50,100,
 　200,500,1000,2000,5000,
 　10000,20000,30000,40000,50000,
 　60000,70000,80000,90000,100000.

## 试题 算法训练 Rotatable Number

 			

   		

资源限制

时间限制：1.0s  内存限制：256.0MB

问题描述

　　Bike是个十分喜欢数学的聪明孩子。他发明了“可旋转数”，其灵感来自于142857。
 　正如你所见，142857是一个十分神奇的数，因为所有从它通过旋转得到的数都是它自己乘以1,2,3...,6（从1到数的长度）。旋转一个数就是将它的最后一位数字放到最前面。比如说，通过旋转12345你能够得到这些数：12345,51234,45123,34512,23451。值得一提的是这里允许有前导0。因而4500123和0123450都能够通过旋转0012345得到。你可以看看142857满足条件的原因了。下面的6个方程都在十进制下成立：
 　142857 * 1 = 142857;
 　142857 * 2 = 285714;
 　142857 * 3 = 428571;
 　142857 * 4 = 571428;
 　142857 * 5 = 714285;
 　142857 * 6 = 857142
 　现在，Bike提出了一个问题。他将“可旋转数”推广到了任意进制b。如上所示，142857是十进制下的一个“可旋转数”。另外一个例子是二进制下的0011。下面的4个方程都在二进制下成立：
 　0011 * 1 = 0011;
 　0011 * 10 = 0110;
 　0011 * 11 = 1001;
 　0011 * 100 = 1100
 　他想要找到最大的b(1 < b < x)，满足在b进制下存在一个长度为n的正“可旋转数”（允许有前导零）。

输入格式

　　仅一行包含两个用空格分隔的整数n,x。

输出格式

　　一行一个整数，表示你找到的最大的b。如果不存在满足条件的b，输出-1。

样例输入I

　　6 11

样例输出I

　　10

样例输入II

　　5 8

样例输出II

　　-1

数据规模和约定

　　对于20%的数据，n <= 10, x <= 15
 　对于50%的数据，x <= 10
 　对于100%的数据，1 <= n <= 5 * 10^6，2 <= x <= 10^9