class Solution {
public:
    bool buddyStrings(string A, string B) {
        if(A.size() != B.size())
        {
            return false;
        }
        int i = -1, j = -1, k = 0;
        unordered_map<char, int> m;
        bool flag = false;
        while(k < A.size())
        {
            m[A[k]]++;
            if(m[A[k]] >= 2)
                flag = true;
            if(A[k] != B[k])
            {
                if(i == -1)
                    i = k;
                else if(j == -1)
                    j = k;
                else
                    return false;
            }
            k++;
        }
        
        if(i == -1 && j == -1)
        {
            return flag;
        }        
        return A[i] == B[j] && A[j] == B[i];
    }
};
