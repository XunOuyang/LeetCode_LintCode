class Solution {
public:
    vector<vector<int>> diagonalSort(vector<vector<int>>& mat) {
        int m = mat.size(), n = mat[0].size();
        unordered_map<int, vector<int>> mp;
        for(int i=0; i < m; i++)
        {
            for(int j =0; j < n; j++)
            {
                mp[i - j].push_back(mat[i][j]);
            }
        }
        for(auto& item:mp)
        {
            sort(item.second.begin(), item.second.end(), greater());
        }
        for(int i=0; i < m; i++)
        {
            for(int j =0; j < n; j++)
            {
                mat[i][j] = mp[i-j].back();
                mp[i-j].pop_back();
            }
        }
        return mat;
    }
};
