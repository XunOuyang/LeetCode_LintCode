// 这道题的精华在于 C++ 里面 iterator 的erase操作。 it = m.erase(it)。代码19行到25行。

class Solution {
public:
    vector<int> majorityElement(vector<int>& nums)
    {
        int k = 2;
        unordered_map<int, int> m;
        for(int i=0; i < nums.size(); i++)
        {
            if(m.find(nums[i]) == m.end() && m.size() < k)
            {
                m[nums[i]] = 1;
            }
            else if(m.find(nums[i]) != m.end()){
                m[nums[i]] += 1;
            }
            else{
                for(auto it=m.begin(); it != m.end();)
                {
                    it->second--;
                    if(it->second == 0)
                        it = m.erase(it);
                    else
                        it++;
                }
            }
        }
        for(auto it=m.begin(); it != m.end(); it++)
        {
            it->second = 0;
        }
        
        vector<int> res;
        for(auto num:nums)
        {
            if(m.find(num) != m.end())
                m[num]++;
        }
        
        for(auto it=m.begin(); it != m.end(); it++)
        {
            if(it->second > nums.size() / (k + 1.0))
                res.push_back(it->first);
        }
        return res;
    }
};
