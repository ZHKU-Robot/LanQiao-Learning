# 直接插入排序
![img](img/1.gif)  

## python实现
其实算法思路也很简单，就是一个比较的关系 ，如果比较不成功，向前移，如果比较成功，则交换。

这里给出两种思路

### 思路1：如上图gif一样交换
```
class Solution:
    #直接插入排序
    def Straight_InsertionSort(self, nums: list) -> int:
        for i in range(1,len(nums)):
            # 从左到右 逐渐遍历
            j=i
            while(j>0):#直到遇见两个相邻变量满足小于关系时交换
                if(nums[j]<nums[j-1]):
                     nums[j - 1], nums[j] = nums[j], nums[j - 1]
                     j = j - 1
                else:
                    break
        return nums
```
### 思路2:向有序数组中插入无序数组
```
    #直接插入一个无序数组到有序数组中
    def Straight_InsertionArray(self,nums,insert):
        for innum in insert:
            for numi in range(len(nums)-1,-1,-1):
                if(innum<nums[0]):
                    nums.insert(0,innum)
                    break
                if(innum>=nums[numi]):
                    nums.insert(numi+1,innum)
                    break
        return  nums
```
## C/C++实现
```
#include<iostream>
using namespace std;
int main()
{
    int a[]={98,76,109,34,67,190,80,12,14,89,1};
    int k=sizeof(a)/sizeof(a[0]);
    int i,j;
    for(i=1;i<k;i++)//循环从第2个元素开始
    {
        if(a[i]<a[i-1])
        {
            int temp=a[i];
            for(j=i-1;j>=0 && a[j]>temp;j--)
            {
                a[j+1]=a[j];
            }
            a[j+1]=temp;//此处就是a[j+1]=temp;
        }
    }
    for(int f=0;f<k;f++)
    {
        cout<<a[f]<<"  ";
    }
    return 0;
}
```