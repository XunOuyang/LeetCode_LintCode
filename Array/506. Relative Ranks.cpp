// This is a very simple coding problem. However coding in C++ is way much more complicated than coding in Python.
// The vector of pair can be sorted by calling sort() directly. Be careful about all the details.

class Solution {
public:
    vector<string> findRelativeRanks(vector<int>& nums) {
        vector<string> res(nums.size(), "");
        vector<pair<int, int>> ranks;
        for(int i=0; i<nums.size(); i++) {
            ranks.push_back(make_pair(nums[i], i));
        }
        sort(ranks.begin(), ranks.end());
        int count = 1;
        while(!ranks.empty()) {
            if(count == 1)
                res[ranks.back().second] = "Gold Medal";
            else if(count == 2)
                res[ranks.back().second] = "Silver Medal";
            else if(count == 3)
                res[ranks.back().second] = "Bronze Medal";
            else
                res[ranks.back().second] = std::to_string(count);
            ranks.pop_back();
            count++;
        }
        return res;
    }
};
