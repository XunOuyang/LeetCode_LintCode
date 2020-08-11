class Solution1 {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int target = 0;
        queue<pair<int, int>> rotten;
        for(int i=0; i<grid.size(); i++)
        {
            for(int j=0; j<grid[0].size(); j++)
            {
                if(grid[i][j] == 1)
                    target++;
                else if(grid[i][j] == 2)
                    rotten.push(make_pair(i, j));
            }
        }
        if(!target)
            return 0;
        if(rotten.size() == 0)
            return -1;
        int res = 0;
        while(!rotten.empty())
        {
            int k = rotten.size();
            while(k--)
            {
                auto pair = rotten.front();
                rotten.pop();
                int x = pair.first, y = pair.second;
                if(x-1 >= 0 && grid[x-1][y] == 1)
                {
                    rotten.push(make_pair(x-1, y));
                    grid[x-1][y] = 2;
                    target -= 1;
                }
                if(y-1 >= 0 && grid[x][y-1] == 1)
                {
                    rotten.push(make_pair(x, y-1));
                    grid[x][y-1] = 2;
                    target -= 1;
                }
                if(x+1 < grid.size() && grid[x+1][y] == 1)
                {
                    rotten.push(make_pair(x+1, y));
                    grid[x+1][y] = 2;
                    target -= 1;
                }
                if(y+1 < grid[0].size() && grid[x][y+1] == 1)
                {
                    rotten.push(make_pair(x, y+1));
                    grid[x][y+1] = 2;
                    target -= 1;
                }
            }
            res += 1;
            if(!target)
                return res;
        }
        return -1;
    }
};


/*
这道题如下的解法（类似于自己平时喜欢用的python的解题套路，也是没有问题的）
并不会因为每一次循环所使用的新的vector是来自于上一次循环的老的vector而导致内存泄漏的问题。
*/
class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int target = 0;
        vector<pair<int, int>> rotten;
        for(int i=0; i<grid.size(); i++)
        {
            for(int j=0; j<grid[0].size(); j++)
            {
                if(grid[i][j] == 1)
                    target++;
                else if(grid[i][j] == 2)
                    rotten.push_back(make_pair(i, j));
            }
        }
        if(!target)
            return 0;
        if(rotten.size() == 0)
            return -1;
        int res = 0;
        while(!rotten.empty())
        {
            vector<pair<int, int>> rotten_new;
            while(!rotten.empty())
            {
                auto pair = rotten.back();
                rotten.pop_back();
                int x = pair.first, y = pair.second;
                
                if(x-1 >= 0 && grid[x-1][y] == 1)
                {
                    rotten_new.push_back(make_pair(x-1, y));
                    grid[x-1][y] = 2;
                    target -= 1;
                }
                if(y-1 >= 0 && grid[x][y-1] == 1)
                {
                    rotten_new.push_back(make_pair(x, y-1));
                    grid[x][y-1] = 2;
                    target -= 1;
                }
                if(x+1 < grid.size() && grid[x+1][y] == 1)
                {
                    rotten_new.push_back(make_pair(x+1, y));
                    grid[x+1][y] = 2;
                    target -= 1;
                }
                if(y+1 < grid[0].size() && grid[x][y+1] == 1)
                {
                    rotten_new.push_back(make_pair(x, y+1));
                    grid[x][y+1] = 2;
                    target -= 1;
                }
            }
            res += 1;
            if(!target)
                return res;
            rotten = rotten_new;
        }
        return -1;
    }
};
