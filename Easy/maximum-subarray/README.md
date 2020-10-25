# [53. 最大子序和](https://leetcode-cn.com/problems/maximum-subarray/)
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

Example 1:

```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```
Example 2:

```
Input: nums = [1]
Output: 1
```
Example 3:

```
Input: nums = [0]
Output: 0
```
Example 4:

```
Input: nums = [-1]
Output: -1
```
Example 5:

```
Input: nums = [-2147483647]
Output: -2147483647
```

进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

Constraints:
```
1 <= nums.length <= 2 * 104
-231 <= nums[i] <= 231 - 1
```
通过次数351,317提交次数667,718

## python
这道题很明显，第一个思路也只能是滑动窗口暴力遍历，除此之外就很离谱，还要我用O(n)的复杂度,我怎么觉得我的思路就是O(n2)

### 学到现在了，是不愿意直接用暴力法的，一定要摒弃这种思想！！

## 但是..
# 看到这题难度为简单，我陷入了沉思! 
# 思考了30分钟我一行代码没写出来，我又陷入了沉思
