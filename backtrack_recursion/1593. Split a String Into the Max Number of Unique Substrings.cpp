// 非常好的一个backtrack的经典题。用C++写起来跟python很不一样。
class Solution {
public:
    int ans = 0;
    void backtrack(string s, int index, unordered_set<string>& us, int words)
    {
        if(index >= us.size())
        {
            ans = max(ans, words);
        }
        string current = "";
        for(int i=index; i < s.size(); i++)
        {
            current += s[i];
            if(us.count(current) == 0)
            {
                us.insert(current);
                backtrack(s, i + 1, us, words + 1);
                us.erase(current);
            }
        }
    }
    int maxUniqueSplit(string s) {
        unordered_set<string> us;        
        backtrack(s, 0, us, 0);
        return ans;
    }
};
