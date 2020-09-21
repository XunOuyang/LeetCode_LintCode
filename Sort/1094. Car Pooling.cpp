// 这种题目不要起手就想着去sort数组。有sort的直觉是非常好的，但是应该先考虑处理后的结果的表达形式是什么样子的，然后再去进一步处理。
// 这道题如果仔细读题，还应该发现，1 <= trips[i][1] < trips[i][2] <= 1000。所以甚至可以不用sort，不用map，而用一个一个数组就足够了。
// 在这里点上，有点类似skyline，可以回味一下。需要时刻记得，c++里面的map是自动sort好的。
class Solution {
public:
    bool carPooling(vector<vector<int>>& trips, int capacity) {
        map<int, int> m;
        for(auto trip:trips)
        {
            m[trip[1]] += trip[0];
            m[trip[2]] -= trip[0];
        }
        for(auto i:m)
        {
            capacity -= i.second;
            if(capacity < 0)
                return false;            
        }
        return true;
    }
};
