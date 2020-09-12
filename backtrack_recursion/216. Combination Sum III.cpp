class Solution {
public:
    vector<vector<int>> res;
    void combination(int k, int n, int index, vector<int> path)
    {
        if(n < 0)
            return ;
        else if(n == 0 && path.size() == k)
            res.push_back(path);
        else
        {
            for(int i = index; i < 10; i++)
            {
                if(path.empty() || (!path.empty() && i > path.back()))
                {
                    path.push_back(i);
                    combination(k, n - i, index + 1, path);
                    path.pop_back();
                }                
            }
        }
    }
    
    vector<vector<int>> combinationSum3(int k, int n) {
        vector<int> path;
        combination(k, n, 1, path);
        return res;
    }   
};
