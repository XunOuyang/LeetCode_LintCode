class Solution {
public:
    int rob(vector<int>& nums) {
        if(nums.size() == 0)
            return 0;
        else if(nums.size() == 1)
            return nums[0];
        int pre = 0, cur = 0, res = 0;
        for(int i=0; i<nums.size(); i++)
        {
            int temp = max(cur, pre + nums[i]);
            pre = cur;
            cur = temp;
        }
        return cur;
    }
};
