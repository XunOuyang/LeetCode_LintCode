class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<int> res;
        vector<int> indegree(numCourses);
        vector<vector<int>> edge(numCourses);
        for(auto prerequisite:prerequisites)
        {
            indegree[prerequisite[0]]++;
            edge[prerequisite[1]].push_back(prerequisite[0]);
        }
        stack<int> s;
        for(int i=0; i < numCourses; i++)
        {
            if(indegree[i] == 0)
            {
                res.push_back(i);
                s.push(i);
            }
        }
        while(!s.empty())
        {
            int temp = s.top();
            s.pop();
            for(auto i:edge[temp])
            {
                indegree[i]--;
                if(indegree[i] == 0)
                {
                    res.push_back(i);
                    s.push(i);
                }
            }            
        }
        if(res.size() == numCourses)
            return res;
        res = {};
        return res;
    }
};
