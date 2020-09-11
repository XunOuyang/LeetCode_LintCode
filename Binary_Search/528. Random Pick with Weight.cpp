//特别需要注意upper_bound 和lower_bound的区别

class Solution {
public:
    vector<int> weights;
    Solution(vector<int>& w) {        
        for(auto index:w)
        {
            if(weights.empty())
                weights.push_back(index);
            else
                weights.push_back(weights.back() + index);
        }
    }
    
    int pickIndex() {
        int x = weights.back();
        int index = rand() % x;
        auto it = upper_bound(weights.begin(), weights.end(), index);
        return it - weights.begin();
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(w);
 * int param_1 = obj->pickIndex();
 */
