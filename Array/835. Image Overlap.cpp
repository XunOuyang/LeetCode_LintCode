#include <map>
class Solution {
public:
    int largestOverlap(vector<vector<int>>& A, vector<vector<int>>& B) {
        vector<pair<int, int>> a, b;
        for(int i=0; i < A.size(); i++)
        {
            for(int j=0; j < A.size(); j++)
            {
                if(A[i][j] == 1)
                    a.push_back(make_pair(i, j));
                if(B[i][j] == 1)
                    b.push_back(make_pair(i, j));
            }
        }
        map<pair<int, int>, int> m;
        int res = 0;
        for(auto x:a)
        {
            for(auto y:b)
            {
                m[make_pair(x.first-y.first, x.second-y.second)] += 1;
                res = max(res, m[make_pair(x.first-y.first, x.second-y.second)]);
            }
        }
        return res;
    }
};
