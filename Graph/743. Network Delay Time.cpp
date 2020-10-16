// 这道题做清楚题目之前一定要弄清楚两点，1，有没有可能出现环？
// 2. 初始化的时候是从1 到 N 而不是0 到 N-1
class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int N, int K) {
        vector<int> visited(N, -1);
        deque<int> q;
        q.push_back(K-1);
        unordered_map<int, vector<pair<int, int>>> m;
        for(auto time:times)
        {
            m[time[0] - 1].push_back(make_pair(time[1] - 1, time[2]));
        }
        visited[K-1] = 0;
        while(!q.empty())
        {
            int node = q.front();
            q.pop_front();
            if(m.find(node) != m.end())
            {
                for(auto item:m[node])
                {
                    if(visited[item.first] == -1 || visited[item.first] > visited[node] + item.second)
                    {
                        visited[item.first] = visited[node] + item.second;
                        q.push_back(item.first);
                    }                        
                }
            }
        }
        if(*min_element(visited.begin(), visited.end()) == -1)
            return -1;
        return *max_element(visited.begin(), visited.end());
    }
};
