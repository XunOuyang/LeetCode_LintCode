This is the standard template for binary search.

For a typical binary search problem, find a target from a vector:

```
int find(vector<int>& nums, int target) {
    int left = 0, right = nums.size() - 1;
    while(left <= right) {
        int mid = left + (right - left)/2
        if(nums[mid] == target)
            return mid;
        if(nums[mid] < target)
            left = mid + 1;
        else
            right = mid - 1;
    return -1;
```

Find first element which equals to the target in an array:
In this case, obvious we cannot just return nums[mid] which equal to the target because duplicates might exist.
```
int find(vector<int>& nums, int target) {
    int left = 0, right = nums.size() - 1;
    while(left <= right) {
        int mid = left + (right - left)/2
        if(nums[mid] < target)
            left = mid + 1;
        else
            right = mid - 1;
    if nums[left] == target:
        return left;
    return -1;
```

Find the last element which equals to the target in an array:
Similar to the case listed above, just try to find the last element which equals to the target
```
int find(vector<int>& nums, int target) {
    int left = 0, right = nums.size() - 1;
    while(left <= right) {
        int mid = left + (right - left)/2
        if(nums[mid] <= target)
            left = mid + 1;
        else
            right = mid - 1;
    if nums[right] == target:
        return right;
    return -1;
```

The template above cannot solve all the problems. 
