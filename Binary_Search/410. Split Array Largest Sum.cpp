For this problem, we are about to looking for the first target of the array. 
```
class Solution {
public:
    int splitArray(vector<int>& nums, int m) {
        long left = 0, right = 0;
        for(auto num:nums) {
            if(num > left) 
                left = num;
            right += num;
        }
        long mid = -1;
        while (left <= right) {
            mid = (right - left)/2 + left;
            long temp = 0;
            int count = 0;
            for(auto num:nums) {
                if(temp + num <= mid) {
                    temp += num;
                }
                else {
                    temp = num;
                    count += 1;
                }
                if(count > m)
                    break;
            }
            if(count < m)
                right = mid - 1;
            else
                left = mid + 1;
        }
        return int(left);
    }
};
```
