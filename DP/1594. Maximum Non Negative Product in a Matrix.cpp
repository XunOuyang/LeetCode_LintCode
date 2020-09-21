// 这道题有三个需要注意的点：
// 1. mod 10**9 + 7 在c++里面的写法是10e9 + 7
// 2. 10e9 + 7 是long 型的
// 3. 因为要求最后的结果才mod 10e9 + 7，所以我们dp的里面就需要long型去存储数据才行。
class Solution {
public:
    int maxProductPath(vector<vector<int>>& grid) {
        int res = 0;
        int m = grid.size(), n = grid[0].size();
        vector<vector<long>> v(n, {INT_MIN, INT_MAX});
        v[0][0] = grid[0][0];
        v[0][1] = grid[0][0];
        for(int j = 1; j < n; j++)
        {
            v[j][0] = v[j-1][0] * grid[0][j];
            v[j][1] = v[j-1][0] * grid[0][j];
        }
        for(int i=1; i < m; i++)
        {
            for(int j = 0; j < n; j++)
            {
                if(j)
                {
                    long x = max(v[j-1][1] * grid[i][j], v[j][1] * grid[i][j]);
                    x = max(x, v[j-1][0] * grid[i][j]);
                    x = max(x, v[j][0] * grid[i][j]);
                    long y = min(v[j-1][1] * grid[i][j], v[j][1] * grid[i][j]);
                    y = min(y, v[j-1][0] * grid[i][j]);
                    y = min(y, v[j][0] * grid[i][j]);
                    v[j][0] = x;
                    v[j][1] = y;
                }
                else
                {
                    v[j][0] = v[j][0] * grid[i][j];
                    v[j][1] = v[j][1] * grid[i][j];
                }
            }   
        }
        if(v[n-1][0] < 0)
            return -1;
        return v[n-1][0] % long(1e9 + 7);
    }
};
