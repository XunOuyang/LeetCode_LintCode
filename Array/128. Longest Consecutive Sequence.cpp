class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_map<int, int> m;
        int res = 0;
        for(auto num:nums) {
            if(! m[num]) {
                m[num] = m[num+m[num+1]] + 1 + m[num-m[num-1]];
                if(m[num+m[num+1]])
                    m[num+m[num+1]] = m[num];
                if(m[num-m[num-1]])
                    m[num-m[num-1]] = m[num];
                res = max(res, m[num]);
            }
        }
        return res;
    }
};
