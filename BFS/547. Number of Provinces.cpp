class Solution {
public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        int n = isConnected.size();
        vector<bool> visited(n, false);
        int res = 0;
        for(int i=0; i < n; i++)
        {
            if(!visited[i])
            {
                check(i, isConnected, visited);
                res += 1;
            }
        }
        return res;
    }
    
    void check(int i, vector<vector<int>>& isConnected, vector<bool>& visited)
    {
        visited[i] = true;
        queue<int> q;
        q.push(i);
        while(!q.empty())
        {
            int index = q.front();
            q.pop();
            for(int j = 0; j < isConnected.size(); j++)
            {
                if(isConnected[index][j] == 1 && visited[j] == false)
                {
                    q.push(j);
                    visited[j] = true;
                }
            }
        }
    }
};
