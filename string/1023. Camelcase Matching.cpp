class Solution {
private:
    bool matching(string query, string pattern) {
        int j = 0;
        for(int i=0; i<query.size(); i++) {
            if(query[i] == pattern[j]) {
                j++;
            }
            else if(query[i] > 'z' || query[i] < 'a')
                return false;
        }
        return j == pattern.size();
    }
public:
    vector<bool> camelMatch(vector<string>& queries, string pattern) {
        vector<bool> res;
        for(string query:queries)
        {
            if(matching(query, pattern))
                res.push_back(true);
            else
                res.push_back(false);
        }
        return res;
    }
};
