/* Solution 1 is preferred. But still be very careful about the recursioin function. The for loop
int the recursion function should start from 0 instead of index. Think about why !
*/

class Solution1 {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> visited(nums.size(), 0);
        vector<int> path;
        recursion(nums, 0, res, visited, path);
        return res;
    }
    
    void recursion(vector<int>& nums, int index, vector<vector<int>>& res, vector<int>& visited, vector<int>& path)
    {
        if(path.size() == nums.size())
        {
            res.push_back(path);
            return ;
        }
        for(int i=0; i<nums.size(); i++)
        {
            if(!visited[i])
            {
                visited[i] = 1;
                path.push_back(nums[i]);
                recursion(nums, index+1, res, visited, path);
                visited[i] = 0;
                path.pop_back();
            }
        }
    }
};

/*
Be careful with the swap function. This idea only works under C++ because C++ can swap the value of elements in
nums, not in the references. While we were trying to implement it in Python, we have to figure out something else
instead. Actually this method is not a very good one.
*/

class Solution2 {
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
