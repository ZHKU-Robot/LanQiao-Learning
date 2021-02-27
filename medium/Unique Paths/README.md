#### [62. Unique Paths](https://leetcode-cn.com/problems/unique-paths/)

A robot is located at the top-left corner of a `m x n` grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time.  The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

 

**Example 1:**

![img](img/robot_maze.png)

```
Input: m = 3, n = 7
Output: 28
```

**Example 2:**

```
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
```

**Example 3:**

```
Input: m = 7, n = 3
Output: 28
```

**Example 4:**

```
Input: m = 3, n = 3
Output: 6
```

 

**Constraints:**

- `1 <= m, n <= 100`
- It's guaranteed that the answer will be less than or equal to `2 * 109`.





很明显，跟走楼梯是一个道理的，但是多了一个维度罢了，那么，我们再次按照三部曲



1. 建立状态转移方程
2. 缓存并复用以往结果
3. 按顺序从小往大算



这里的状态转移方程倒是很容易看出来，有了之前走楼梯的经验

机器人走到终点 只能通过向下和向右走，那么，我们分解一下

走到终点前 必然是向右走到，或者向下走到，也就是说，走到终点是由走到终点左一个格子的路径数+走到终点上一个格子的路径数之和！



> ### **最优子结构**
>
> 我们仍以「宝石挑选」例题来讲解这两大原则，首先是「最优子结构」。
>
> 什么是「最优子结构」？将原有问题化分为一个个子问题，即为子结构。而对于每一个子问题，其最优值均由「更小规模的子问题的最优值」推导而来，即为最优子结构。
>
> 因此「DP 状态」设置之前，需要将原有问题划分为一个个子问题，且需要确保子问题的最优值由「更小规模子问题的最优值」推出，此时子问题的最优值即为「DP 状态」的定义。
>
> 作者：力扣（LeetCode）
> 链接：https://www.zhihu.com/question/39948290/answer/1309260344
> 来源：知乎
> 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



也就是说，我哦们可以找到小规模的问题，自底向上的找到最优解

理解的过程中找到很多宝藏

> https://zhuanlan.zhihu.com/p/78220312
>
> **明确 base case -> 明确「状态」-> 明确「选择」 -> 定义 dp 数组/函数的含义**。
>
> 按上面的套路走，最后的结果就可以套这个框架：
>
> ```reStructuredText
> # 初始化 base case
> dp[0][0][...] = base
> # 进行状态转移
> for 状态1 in 状态1的所有取值：
>     for 状态2 in 状态2的所有取值：
>         for ...
>             dp[状态1][状态2][...] = 求最值(选择1，选择2...)
> ```

1.  **确定 base case** 
2.  **确定「状态」，也就是原问题和子问题中会变化的变量** 
3.  **确定「选择」，也就是导致「状态」产生变化的行为** 
4.  **明确 `dp` 函数/数组的定义** 

大概就是这样

