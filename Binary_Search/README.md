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
