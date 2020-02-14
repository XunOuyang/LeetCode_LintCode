class Solution {
public:
    int totalNQueens(int n) {
        vector<string> board(n, string(n, '.'));   // build the board correctly means half of the problem got resolved.
        int res = 0;        // attension, res need to be initialized here.
        backtrack(res, 0, n, board);
        return res;
    }
    
    void backtrack(int& res, int row, int& n, vector<string>& board) {
        if(row == n) {
            res++;
            return;
        }
        for(int i=0; i<n; i++) {
            if(isValid(board, row, i, n)) {
                board[row][i] = 'Q';
                backtrack(res, row+1, n, board);
                board[row][i] = '.';
            }
        }
    }
    
    bool isValid(vector<string>&board, int row, int col, int& n) {
        for(int i=0; i<row; i++) {
            if(board[i][col] == 'Q')
                return false;
        }
        for(int i=0; i<row; i++) {
            if(col-row+i >= 0 && board[i][col-row+i] == 'Q')
                return false;
        }
        for(int i=0; i<row; i++) {
            if(col+row-i < n && board[i][col+row-i] == 'Q')
                return false;
        }
        return true;
    }
};
