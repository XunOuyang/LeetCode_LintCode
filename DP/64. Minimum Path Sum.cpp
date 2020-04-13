// 这应该是DP里面，最最最经典，最最最典型的一道题（除了斐波那契数列）。
// 从二维降为到一维，看似简单，但是实际上很容易犯非常多的错误。
// 从两个一维降到一个一维的空间，implement也非常容易犯错。其实中间并没有什么算法的改进了，只是看到了变量运用的浪费，可以节约更多的空间罢了。

class Solution2 {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        if(m <= 0 || n <= 0)
            return 0;
        vector<vector<int>> dp(m, vector<int> (n, 0));
        dp[0][0] = grid[0][0];
        for(int i=1; i<m; i++)
            dp[i][0] = grid[i][0] + dp[i-1][0];
        for(int i=1; i<n; i++)
            dp[0][i] = grid[0][i] + dp[0][i-1];
        for(int i=1; i<m; i++)
            for(int j=1; j<n; j++)
                dp[i][j] = min(dp[i-1][j]+grid[i][j], dp[i][j-1]+grid[i][j]);
        return dp[m-1][n-1];
    }
};

class Solution1 {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        if(m <= 0 || n <= 0)
            return 0;
        vector<int> pre(n, grid[0][0]);
        vector<int> cur(n, 0);
        for(int i=1; i<n; i++)
            pre[i] = grid[0][i] + pre[i-1];
        for(int i=1; i<m; i++)
        {
            cur[0] = grid[i][0] + pre[0];
            for(int j=1; j<n; j++)
            {
                cur[j] = min(pre[j], cur[j-1]) + grid[i][j];
            }
            pre = cur;
        }
        return pre[n-1];
    }
};

class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        if(m <= 0 || n <= 0)
            return 0;
        vector<int> cur(n, grid[0][0]);
        for(int i=1; i<n; i++)
            cur[i] = grid[0][i] + cur[i-1];
        for(int i=1; i<m; i++)
        {
            cur[0] = grid[i][0] + cur[0];
            for(int j=1; j<n; j++)
            {
                cur[j] = min(cur[j], cur[j-1]) + grid[i][j];
            }
        }
        return cur[n-1];
    }
};
