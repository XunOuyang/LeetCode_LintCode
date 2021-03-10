class Solution {
public:
    int findSubstringInWraproundString(string p) {
        int res = 0;
        if(p.size() == 0)
            return 0;
        vector<int> count(26, 0);
        int temp = 1;
        for(int i=0; i < p.size(); i++)
        {
            if(i && (p[i] - p[i-1] == 1 || p[i] - p[i-1] == -25))
                temp += 1;
            else
            {
                temp = 1;
            }
            count[p[i] - 'a'] = max(temp, count[p[i] - 'a']);
        }
        for(int i=0; i < 26; i++)
        {
            res += count[i];
        }
        return res;
    }
};
