# -*- coding: utf-8 -*-
"""
Created on Fri May 18 18:15:20 2018

@author: tzlmyq
"""

这道题不难，但是确实一个极其容易出错的题目。
容易出错在哪里呢？
我们都知道一定要做两次反转，两种解法：
1. 左右翻转，然后沿着右上到左下的轴做对称翻转。
2. 上下翻转，然后沿着左上到右下的轴做对称翻转。
两种解法都可以，但是由于边界条件，比较容易出错。
```
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int size = matrix.size();
        for(int i=0; i < size; i++) {
            for(int j=0; j < size / 2; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[i][size - j - 1];
                matrix[i][size - j - 1] = temp;
            }
        }
        for(int i=0; i < size; i++) {
            for(int j=0; j < size - 1 - i; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[size - j - 1][size - i - 1];
                matrix[size - j - 1][size - i - 1] = temp;
            }
        }
    }
};
```

```
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        print matrix
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
class Solution2:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(len(matrix)):
            for j in range(len(matrix)//2):
                matrix[i][j], matrix[i][len(matrix)-1-j] = matrix[i][len(matrix)-1-j], matrix[i][j]
        return matrix

matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
solution = Solution()
solution.rotate(matrix)
```
                

