#include <stdio.h>
#include <stdlib.h>
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

int *twoSum(int *nums, int numsSize, int target, int *returnSize)
{
}
int main()
{
    int nums[] = {-1,-2,-3,-4,-5}, target = -8, *returnSize, *arr;
    int numsSize = sizeof(nums) / sizeof(int);
    arr = twoSum(nums, numsSize, target, returnSize);
    printf("1.=%d,\n2.=%d", arr[0], arr[1]);
}