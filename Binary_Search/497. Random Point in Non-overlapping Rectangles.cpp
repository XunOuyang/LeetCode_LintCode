// 这道题两个重点：
// 1. 如何在一个类初始化的时候给变量赋值
// 2. 搞清楚什么情况用upper_bound，什么情况用lower_bound，以及，要找到pos，需要用upper_bound lower_bound - v.begin()，
class Solution {
public:
    vector<int> v;
    int total = 0;
    vector<vector<int>> rects;
    Solution(vector<vector<int>>& rects):rects(rects) {
        for(auto rect:rects)
        {
            total += (rect[2] - rect[0] + 1) * (rect[3] - rect[1] + 1);
            v.push_back(total);
        }
    }
    
    vector<int> pick() {
        int pos = upper_bound(v.begin(), v.end(), rand() % total) - v.begin();
        vector<int> res;
        int x = rand() % (rects[pos][2] - rects[pos][0] + 1) + rects[pos][0];
        int y = rand() % (rects[pos][3] - rects[pos][1] + 1) + rects[pos][1];
        res.push_back(x);
        res.push_back(y);
        return res;
    }
};
