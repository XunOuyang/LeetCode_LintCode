class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        set<string> st;
        vector<bool> v(s.size() + 1, false);
        if(s.size() && wordDict.size())
            v[0] = true;
        else
            return false;
        for(auto word:wordDict)
            st.insert(word);
        for(int i = 0; i < s.size(); i++)
        {
            for(int j = i + 1; j < s.size() + 1; j++)
            {
                if(v[i] && st.count(s.substr(i, j - i)))
                {
                    v[j] = true;
                }
            }
        }
        return v[s.size()];
    }
};
