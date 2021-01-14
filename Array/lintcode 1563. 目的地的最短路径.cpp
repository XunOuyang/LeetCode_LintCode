// 最简单的BFS题目。但是写的时候依然出现了问题。visited 在c++中不能够用unordered_set，而应该用vector<vector<int>> 不知道未来类似的情况如何使用hash。
// 

#include <utility>
using namespace std;

class Solution {
public:
    /**
     * @param targetMap: 
     * @return: nothing
     */
    int shortestPath(vector<vector<int>> &targetMap) {
        // Write your code here
        queue<pair<int, int>> q;
        pair<int, int> p = make_pair(0, 0);
        q.push({0, 0});
        int res = 0;
        vector<vector<int>> visited(targetMap.size(), vector<int>(targetMap[0].size(), 0));
        while(!q.empty())
        {
            queue<pair<int, int>> new_q;
            while(!q.empty())
            {
                int x = q.front().first, y = q.front().second;
                q.pop();
                if(targetMap[x][y] == 2)
                    return res;
                visited[x][y] = 1;
                if(x -1 >= 0 && !visited[x-1][y] && targetMap[x - 1][y] != 1)
                {
                    new_q.push({x - 1, y});
                }
                if(x + 1 < targetMap.size() &&  !visited[x+1][y] && targetMap[x + 1][y] != 1)
                {
                    new_q.push({x + 1, y});
                }
                if(y -1 >= 0 &&  !visited[x][y-1] && targetMap[x][y - 1] != 1)
                {
                    new_q.push({x, y-1});
                }
                if(y+ 1 < targetMap[0].size() &&  !visited[x][y+1] && targetMap[x][y + 1] != 1)
                {
                    new_q.push({x, y + 1});
                }
            }
            res += 1;
            q = new_q;
        }
        return -1;
    }
};
