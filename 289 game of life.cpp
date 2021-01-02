// 一道很容易的题，但是要一次写清楚bug free 同时inplace 的空间复杂度，对自己来说却非常困难。
// 在两个地方卡了很久，1，min这个funciton，要求里面类型一致（这个错误以前就犯过）。
// 2. 计算细胞数量的时候不能计算其本身。
#include <algorithm> 
class Solution {
public:
    void gameOfLife(vector<vector<int>>& board) {
        for(int i=0; i < board.size(); i++)
        {
            for(int j=0; j < board[0].size(); j++)
            {
                update(board, i, j);
            }
        }
        for(int i=0; i < board.size(); i++)
        {
            for(int j=0; j < board[0].size(); j++)
            {
                if(board[i][j] > 0)
                    board[i][j] = 1;
                else
                    board[i][j] = 0;
            }
        }
    }
    
    void update(vector<vector<int>>& board, int x, int y)
    {
        int count = 0;
        for(int i = max(0, x - 1); i <= std::min(x + 1, int(board.size() - 1)); i++)
        {
            for(int j = max(0, y - 1); j <= std::min(y + 1, int(board[0].size() - 1)); j++)
            {
                if(x == i && y == j)
                    continue;
                if(board[i][j] == 1 || board[i][j] == -1)
                    count += 1;
            }
        }
        if(board[x][y] == 1 && (count > 3 || count < 2))
            board[x][y] = -1;
        else if(count == 3 && board[x][y] == 0)
            board[x][y] = 2;
        
    }
};
