// 先在纸上弄明白，到底该怎么排放顺序就可以，搞明白了之后，写出来代码就很快乐。搞明白了之后就会意识到，这是一道贪心法的题目。
class Solution {
public:
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        sort(people.begin(), people.end(), [](const vector<int>& a, const vector<int>&b){return (a[0] > b[0]) || (a[0] == b[0] && a[1] < b[1]);});
        vector<vector<int>> res;
        for(int i = 0; i < people.size(); i++)
        {
            res.insert(res.begin() + people[i][1], people[i]);
        }
        return res;
    }
};
