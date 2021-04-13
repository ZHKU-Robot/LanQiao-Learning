#### [剑指 Offer 15. 二进制中1的个数](https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof/)

请实现一个函数，输入一个整数（以二进制串形式），输出该数二进制表示中 1 的个数。例如，把 9 表示成二进制是 1001，有 2 位是 1。因此，如果输入 9，则该函数输出 2。

 

**示例 1：**

```
输入：00000000000000000000000000001011
输出：3
解释：输入的二进制串 00000000000000000000000000001011 中，共有三位为 '1'。
```

**示例 2：**

```
输入：00000000000000000000000010000000
输出：1
解释：输入的二进制串 00000000000000000000000010000000 中，共有一位为 '1'。
```

**示例 3：**

```
输入：11111111111111111111111111111101
输出：31
解释：输入的二进制串 11111111111111111111111111111101 中，共有 31 位为 '1'。
```

 

**提示：**

- 输入必须是长度为 `32` 的 **二进制串** 。

在python里现成的方法,不过问题是在思想上

```
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')
```

![1618316048822](readme.assets/1618316048822.png)

这里主要考的是位操作 所以 高效 的使用位操作的正确方式是



检测有整数n 多少个1 

```
class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        while n!=0:
            if n&1:
                count+=1
            n=n>>1
        return count

```

![1618317252315](readme.assets/1618317252315.png)

当然这种 O (n) 的 肯定是不满意的 而且可能引起死循环

当输入的是负数时 直接会裂开

所以换一种思考,我们直接左移

还可以用一些奇淫技巧缩短时间

```
class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        while(n):
            count+=1
            n=(n-1)&n
        return count
```

![1618320271042](readme.assets/1618320271042.png)
