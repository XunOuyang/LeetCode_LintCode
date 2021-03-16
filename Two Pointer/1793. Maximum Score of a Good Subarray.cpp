class Solution {
public:
    int maximumScore(vector<int>& nums, int k) {
        int res = nums[k];
        int left = k, right = k;
        int m = nums[k];
        while(left > 0 || right < nums.size() - 1)
        {
            if(left > 0 && ((right < nums.size() - 2 && nums[left-1] >= nums[right + 1]) || right == nums.size() - 1))
            {
                left -= 1;
                m = min(nums[left], m);
                res = max(res, m * (right - left + 1));
            }
            else 
            {
                right += 1;
                m = min(nums[right], m);
                res = max(res, m * (right - left + 1));
            }
        }
        return res;
    }
};
