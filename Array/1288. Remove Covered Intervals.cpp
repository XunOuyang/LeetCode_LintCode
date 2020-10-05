// 这道题主要是学会c++ lambda的写法。
class Solution {
public:
    int removeCoveredIntervals(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), [](vector<int>& a, vector<int>& b){return a[0] < b[0] || a[0] == b[0] && a[1] > b[1];});
        int covered = 0;
        int left = 0, right = 1;
        while(right < intervals.size())
        {
            if(left >= right)
                right++;
            else if(intervals[left][1] < intervals[right][1])
                left++;
            else if(intervals[left][1] >= intervals[right][1])
            {
                covered++;
                right++;
            }
        }
        return intervals.size() - covered;        
    }
};
