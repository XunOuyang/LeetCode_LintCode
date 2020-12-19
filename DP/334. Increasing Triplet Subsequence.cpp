class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        vector<int> dp;
        for(auto& num:nums)
        {
            if(dp.size() == 0)
                dp.push_back(num);
            else if(num <= dp[0])
            {
                dp[0] = num;
            }
            else if(dp.size() == 1)
            {
                dp.push_back(num);
            }
            else if(num <= dp[1])
                dp[1] = num;
            else if(num > dp[1])
                return true;
        }
        return false;
    }
};
