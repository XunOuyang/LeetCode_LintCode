class Solution {
public:
    vector<int> findMinHeightTrees(int n, vector<vector<int>>& edges) {
        if(n == 1)
            return {0};
        unordered_map<int, unordered_set<int>> m;
        for(auto & edge:edges)
        {
            m[edge[0]].insert(edge[1]);
            m[edge[1]].insert(edge[0]);
        }
        vector<int> res;
        for(int i=0; i<n; i++) {
            if(m[i].size() == 1)
                res.push_back(i);
        }
        while(true)
        {
            vector<int> temp;
            for(auto i:res)
            {
                for(auto j:m[i])
                {
                    m[j].erase(i);
                    if(m[j].size() == 1)
                        temp.push_back(j);
                }
            }
            if(temp.size() == 0)
                return res;
            else
            {
                res = temp;
                temp.clear();
            }
        }
    }
};
