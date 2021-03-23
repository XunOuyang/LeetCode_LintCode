class Solution {
public:
    bool isMatch(string s, string p) {
        if(p == "")
            return s == "";
        else if(p.size() > 1 && p[1] == '*')
            return isMatch(s, p.substr(2)) || (!s.empty() && (s[0] == p[0] || p[0] == '.') && isMatch(s.substr(1), p));
        return !s.empty() && (s[0] == p[0] || p[0] == '.') && isMatch(s.substr(1), p.substr(1));    
    }
};
