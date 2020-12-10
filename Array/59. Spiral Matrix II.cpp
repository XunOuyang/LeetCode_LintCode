class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> res(n, vector<int>(n, 0));
        int direction = 1;
        int left_bound = -1, right_bound = n, top_bound = -1, bottom_bound = n;
        int x = 0, y = 0;
        for(int i=1; i <= n * n; i++)
        {
            
            res[x][y] = i;
            if(direction == 1)
            {
                if(y + 1 == right_bound)
                {
                    direction = 2;
                    top_bound++;
                    x++;
                }
                else
                    y++;
            }
            else if(direction == 2)
            {
                if(x + 1 == bottom_bound)
                {
                    direction = 3;
                    right_bound--;
                    y--;
                }
                else
                    x++;
            }
            else if(direction == 3)
            {
                if(y - 1 == left_bound)
                {
                    direction = 4;
                    bottom_bound--;
                    x--;
                }
                else
                    y--;
            }
            else if(direction == 4)
            {
                if(x - 1 == top_bound)
                {
                    direction = 1;
                    left_bound++;
                    y++;
                }
                else
                    x--;
            }
        }
        return res;
    }
};
