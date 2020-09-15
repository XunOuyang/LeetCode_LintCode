class Solution {
public:
    int rob(vector<int>& nums) {
        if(nums.size() == 0)
            return 0;
        int pre_0 = 0, pre_1 = nums[0];
        int res = nums[0];
        for(int i=1; i < nums.size(); i++)
        {
            int temp_0 = max(pre_0, pre_1);
            int temp_1 = max(pre_0 + nums[i], pre_1);
            res = max(temp_0, temp_1);
            pre_0 = temp_0;
            pre_1 = temp_1;        
        }
        return res;
    }
};
