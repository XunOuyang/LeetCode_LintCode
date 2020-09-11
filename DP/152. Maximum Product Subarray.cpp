// Pay attention to the Intermediate varialbe.
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        if(nums.size() == 0)
            return 0;
        int max_prod = nums[0], min_prod = nums[0], res = nums[0];
        for(int i = 1; i < nums.size(); i++)
        {
            int max_temp = max_prod, min_temp = min_prod;
            max_prod = max(nums[i], max(max_temp * nums[i], min_temp * nums[i]));
            min_prod = min(nums[i], min(max_temp * nums[i], min_temp * nums[i]));
            res = max(max_prod, res);
        }
        return res;
    }
};
