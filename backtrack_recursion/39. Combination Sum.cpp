class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<vector<int>> res;
        vector<int> path;
        backtrack(candidates, 0, target, path, res);
        return res;
    }
    
    void backtrack(vector<int>& candidates, int index, int target, vector<int>& path, vector<vector<int>>& res)
    {
        if(path.size() != 0 && target == 0)
        {
            res.push_back(path);
            return ;
        }
        if(target < 0)
            return ;
        for(int i=index; i < candidates.size(); i++)
        {
            path.push_back(candidates[i]);
            backtrack(candidates, i, target - candidates[i], path, res);
            path.pop_back();
        }
    }
};
