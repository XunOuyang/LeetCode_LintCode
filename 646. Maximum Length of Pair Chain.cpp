class Solution {
public:
    int findLongestChain(vector<vector<int>>& pairs) 
    {
        std::sort(pairs.begin(), pairs.end(), cmp);
        int res = 0;
        int temp = INT_MIN;
        cout << temp << endl;
        for(int i=0; i<pairs.size(); i++)
        {
            if(pairs[i][0] > temp)
            {
                temp = pairs[i][1];
                res += 1;
            }
        }
        return res;
    }
private:
    static bool cmp(vector<int>& a, vector<int>& b)
    {
        return a[1] < b[1];
    }  
};
