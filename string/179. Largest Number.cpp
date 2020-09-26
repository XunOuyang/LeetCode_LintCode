// 非常好的一道题，也不难。就是考察lambda的写法
class Solution {
public:
    string largestNumber(vector<int>& nums) {
        string res = "";
        vector<string> s;
        for(auto num:nums)
        {
            s.push_back(to_string(num));
        }
        sort(s.begin(), s.end(), [](string s1, string s2){return s1 + s2 > s2 + s1;});
        for(auto c:s)
            res += c;
        while(res[0] == '0' && res.size() > 1)
            res.erase(0, 1);
        return res;
        
    }
};
