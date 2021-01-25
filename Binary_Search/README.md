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

同一个类型的题目：
Minimum Number of Days to Make m Bouquets
Find the Smallest Divisor Given a Threshold
Divide Chocolate
Capacity To Ship Packages In N Days
Koko Eating Bananas
Minimize Max Distance to Gas Station

[410. Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/)   (这道题跟1011是一模一样的）
[1011. Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/)
