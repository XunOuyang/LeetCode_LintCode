class Solution {
public:
    int lengthOfLastWord(string s) {
        if(s.size() == 0)
            return 0;
        int res = 0;
        bool flag = false;
        for(int i=s.size()-1; i>= 0; i--)
        {
            if(std::isalpha(s[i]))
            {
                flag = true;
                res++;
            }
            else if(flag)
                break;
        }
        return res;
    }
};
