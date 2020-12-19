class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> dp;
        for(auto& num:nums)
        {
            if(dp.size() == 0)
            {
                dp.push_back(num);
            }
            else if(num > dp.back())
                dp.push_back(num);
            else if(num < dp[0])
                dp[0] = num;
            else 
            {
                int i = dp.size() - 1;
                while(i > 0)
                {
                    if(num > dp[i - 1])
                    {
                        dp[i] = num;
                        break;
                    }
                    i--;
                }                
            }
        }
        return dp.size();
    }
};
