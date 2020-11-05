class Solution {
public:
    int minimumEffortPath(vector<vector<int>>& heights) {
        if(heights.size() == 0 || heights[0].size() == 0)
            return 0;
        int res = 0;
        vector<vector<bool>> visited(heights.size(), vector<bool>(heights[0].size(), false));
        visited[0][0] = true;
        priority_queue<pair<int, pair<int, int>>> pq;
        pq.push(make_pair(0, make_pair(0, 0)));
        while(!pq.empty())
        {            
            int val = -pq.top().first;
            int x = pq.top().second.first, y = pq.top().second.second;
            pq.pop();
            visited[x][y] = true;
            res = max(res, val);
            if(x == heights.size() - 1 && y == heights[0].size() - 1)
                return res;
            if(x - 1 >= 0 && !visited[x - 1][y])
                pq.push(make_pair(-abs(heights[x][y] - heights[x - 1][y]), make_pair(x - 1, y)));
            if(x + 1 < heights.size() && !visited[x + 1][y])
                pq.push(make_pair(-abs(heights[x][y] - heights[x + 1][y]), make_pair(x + 1, y)));
            if(y - 1 >= 0 && !visited[x][y - 1])
                pq.push(make_pair(-abs(heights[x][y] - heights[x][y - 1]), make_pair(x, y - 1)));
            if(y + 1 < heights[0].size() && !visited[x][y + 1])
                pq.push(make_pair(-abs(heights[x][y] - heights[x][y + 1]), make_pair(x, y + 1)));            
        }
        return res;
    }
};
