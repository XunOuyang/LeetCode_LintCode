// 下面这个解法注意两点，1.dfs 返回值，返回什么。
// 2. 返回值的简略写法。
class Solution {
public:
    bool dfs(int target, int source, unordered_map<int, vector<int>>& m, vector<vector<int>>& v) {
        
        if (v[source][target] != -1)
            return v[source][target];
        
        for (int i = 0; i < m[source].size(); i++) {
            if (m[source][i] == target || dfs(target, m[source][i], m, v))
                return v[source][target] = 1;
        }
        
        return v[source][target] = 0;
    }
        
    vector<bool> checkIfPrerequisite(int n, vector<vector<int>>& prerequisites, vector<vector<int>>& queries) {
        vector<vector<int>> v(n, vector<int>(n, -1));
        unordered_map<int, vector<int>> m;
        for(auto prerequisite:prerequisites)
        {
            v[prerequisite[1]][prerequisite[0]] = 1;
            m[prerequisite[1]].push_back(prerequisite[0]);
        }
              
        vector<bool> res;
        for(auto query:queries)
        {
            if(dfs(query[0], query[1], m, v))
                res.push_back(true);
            else
                res.push_back(false);
        }
        return res;
    }
};

// 其实应该可以想到这个解法不好。因为空间复杂度相当的大。写起来比较简单，用了拓扑排序。
class Solution1 {
public:
    vector<bool> checkIfPrerequisite(int n, vector<vector<int>>& prerequisites, vector<vector<int>>& queries) {
        map<int, set<int>> m;
        map<int, set<int>> m1;
        vector<int> outdegree(n, 0);
        for(auto prerequisite:prerequisites)
        {
            m[prerequisite[0]].insert(prerequisite[1]);
            m1[prerequisite[1]].insert(prerequisite[0]);  
            outdegree[prerequisite[0]]++;
        }
        stack<int> s;
        for(int i = 0; i < n; i++)
        {            
            if(outdegree[i] == 0)
            {
                s.push(i);
            }                
        }
        while(!s.empty())
        {
            int temp = s.top();
            s.pop();
            for(auto x:m1[temp])
            {            
                outdegree[x]--;
                if(!outdegree[x])
                    s.push(x);
                m[x].insert(m[temp].begin(), m[temp].end());
            }
        }        
        
        vector<bool> res;
        for(auto query:queries)
        {
            if(m[query[0]].count(query[1]))
                res.push_back(true);
            else
                res.push_back(false);
        }
        return res;
    }
};
