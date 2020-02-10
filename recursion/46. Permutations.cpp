"""
Be careful with the swap function. This idea only works under C++ because C++ can swap the value of elements in
nums, not in the references. While we were trying to implement it in Python, we have to figure out something else
instead.
"""

class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res;
        recursion(nums, 0, res);
        return res;
    }
    
    void recursion(vector<int>& nums, int index, vector<vector<int>>& res)
    {
        if(index == nums.size())
        {
            res.push_back(nums);
            return ;
        }
        for(int i=index; i<nums.size(); i++)
        {
            swap(nums[index], nums[i]);
            recursion(nums, index+1, res);
            swap(nums[index], nums[i]);
        }
    }
};
