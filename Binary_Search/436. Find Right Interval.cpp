// 这种题目，遇到用C++解的时候，一定第一直觉反应需要使用map和upper_bound 和lower_bound
class Solution {
public:
    vector<int> findRightInterval(vector<vector<int>>& intervals) {
        map<int, int> m;
        vector<int> res(intervals.size());
        vector<int> index;
        for(int i=0; i< intervals.size(); i++)
        {
            m[intervals[i][0]] = i;
        }
        for(int i=0; i < intervals.size(); i++)
        {
            res[i] = m.lower_bound(intervals[i][1]) != end(m) ? m.lower_bound(intervals[i][1])->second : -1;
        }
        return res;
    }
};
