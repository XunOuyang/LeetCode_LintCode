class Solution {
public:
    int minOperations(vector<int>& target, vector<int>& arr) {
        vector<int> nums;
        unordered_map<int, int> m;
        for(int i=0; i < target.size(); i++)
        {
            m[target[i]] = i;
        }
        vector<int> v;
        for(auto& num:arr)
        {
            if(m.find(num) !=m.end())
            {
                if(v.empty())
                    v.push_back(m[num]);
                else
                {
                    auto pos = lower_bound(v.begin(), v.end(), m[num]);
                    if(pos - v.begin() < v.size())
                    {
                        v[pos - v.begin()] = m[num];
                    }
                    else
                        v.push_back(m[num]);
                }                
            }
        }
        return target.size() - v.size();
    }
};
