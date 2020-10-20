class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        unordered_map<string, int> m;
        vector<string> res;
        if(s.size() < 11)
            return res;
        for(int i=0; i <  s.size() - 9; i++)
        {
            if(m[s.substr(i, 10)] == 1)
                res.push_back(s.substr(i, 10));
            m[s.substr(i, 10)]++;
        }
        return res;
    }
};
