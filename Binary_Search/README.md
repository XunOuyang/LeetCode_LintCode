This is the standard template for binary search.

Best template:


                                        
![binary_search](https://github.com/XunOuyang/LeetCode/blob/master/Binary_Search/image/binary_search.jpg)
```
int left = -1, right = nums.size();
while(left != right - 1)
{
    if(condition1)
        left = mid;
    else
        right = mid;
}
```

经典二分法的题目：
[34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)
