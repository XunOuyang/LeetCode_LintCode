#include <iostream>
#include <queue>
#include <climits>

using namespace std;

class Solution {
public:
    void wallsAndGates(vector<vector<int>>& rooms) {
        queue<pair<int, int>> q;
        for(int i=0; i < rooms.size(); i++) {
            for(int j=0; j<rooms[0].size(); j++) {
                if(rooms[i][j]==0)
                    q.push({i, j});
            }
        }
        
        vector<vector<int>> dis {{0, -1}, {0, 1}, {-1, 0}, {1, 0}};
        
        while(!q.empty()) {
            int i = q.front().first;
            int j = q.front().second;
            q.pop();
            for(int k=0; k < dis.size(); k++) {
                int x = i + dis[k][0];
                int y = j + dis[k][1];
                if(x>=rooms.size() || x <0 || y>=rooms[0].size() || y < 0 || rooms[x][y] <rooms[i][j]+1)
                    continue;
                if(rooms[x][y]!=-1)
                {
                    rooms[x][y] = rooms[i][j]+1;
                    q.push({x, y});
                }
            }
        }
    }
};
    
int main() {
    Solution solution;
    vector<vector<int>> rooms;
    rooms = {{INT_MAX, -1, 0, INT_MAX}, {INT_MAX, INT_MAX, INT_MAX, -1}, {INT_MAX, -1, INT_MAX, -1},{0, -1, INT_MAX, INT_MAX}};
    solution.wallsAndGates(rooms);
    for(int i=0; i < rooms.size(); i++) {
            for(int j=0; j<rooms[0].size(); j++) {
                cout << rooms[i][j] << " ";
            }
            cout << endl;
        }
    
}