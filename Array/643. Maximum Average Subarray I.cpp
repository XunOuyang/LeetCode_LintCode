class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        int sums = 0;
        if(k <= 0)
            return 0;
        sums = std::accumulate(nums.begin(), nums.begin()+k, 0);
        int res = sums;
        for(int i=k; i<nums.size(); i++)
        {
            sums = sums-nums[i-k]+nums[i];
            res = max(sums, res);
        }
        return double(res)/k;
    }
};
