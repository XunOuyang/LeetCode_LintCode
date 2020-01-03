#include <iostream>
#include <vector>
#include <queue>
using namespace std;

class solution
{
public:
    void wallsAndGates(vector<vector<int>>& matrix)
    {
        queue<pair<int, int>> q;
        for(int i=0; i<matrix.size(); i++)
        {
            for(int j=0; j<matrix[0].size(); j++)
            {
                if(matrix[i][j] == 0)
                {
                    q.push({i, j});
                }
            }
        }
        int distance = 0;
        vector<vector<int>> directions{{-1, 0}, {1, 0}, {0, 1}, {0,-1}};
        while(!q.empty())
        {
            int x = q.front().first, y = q.front().second;
            q.pop();
            for(int i=0; i<directions.size(); i++)
            {
                if(x+directions[i][0]<0 || x+directions[i][0]>=matrix.size()
                || y+directions[i][1]<0 || y+directions[i][1]>=matrix[0].size())
                    continue;
                if(matrix[x+directions[i][0]][y+directions[i][1]] > matrix[x][y]+1)
                {
                    matrix[x+directions[i][0]][y+directions[i][1]] = matrix[x][y]+1;
                    q.push(make_pair(x+directions[i][0], y+directions[i][1]));
                }
            }
        }
    }
};
