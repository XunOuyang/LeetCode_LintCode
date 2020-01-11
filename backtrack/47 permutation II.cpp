class Solution {
public:
    
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<vector<int>> res;
        sort(nums.begin(), nums.end());
        backtrack(nums, 0, res);
        return res;
    }
    
    void backtrack(vector<int> nums, int index, vector<vector<int>>& res) {
        if(index==nums.size()-1) {
            res.push_back(nums);
            return ;
        }
        for(int i=index; i<nums.size(); i++) {
            if(nums[index]==nums[i] && i != index)
                continue;
            swap(nums[index], nums[i]);
            backtrack(nums, index+1, res);
        }
    }
};
