/*
Be very careful about this problem espeically compare it with the problem 46. See how do we make sure
that the duplicates are removed.
*/
class Solution {
public:
    
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<vector<int>> res;
        sort(nums.begin(), nums.end());
        vector<int> path;
        vector<int> visited(nums.size(), 0);
        backtrack(nums, 0, path, visited, res);
        return res;
    }
    
    void backtrack(vector<int> nums, int index, vector<int>& path, vector<int>& visited, vector<vector<int>>& res) {
        if(index==nums.size()) {
            res.push_back(path);
            return ;
        }
        for(int i=0; i<nums.size(); i++) {
            if(visited[i])
                continue;
            if(i && nums[i-1]==nums[i] && visited[i-1] == 0)
                continue;
            visited[i] = 1;
            path.push_back(nums[i]);
            backtrack(nums, index+1, path, visited, res);
            path.pop_back();
            visited[i] = 0;
        }
    }
};
