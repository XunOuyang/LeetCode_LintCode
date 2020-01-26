"""
The basic idea is to traverse the matrix diagonally.
How many rows if we count the matrix diagonally ? 
M + N - 1 rows.
It is more like a coordinates transform problem. We have f(x, y) -> g(i, j)
For the first diagonal row, we have 1 elements, 
        second row, 2 elements,
        third row, 3 elements
So how do we get the coordinate formula for each row ?
0 <= i < M+N-1
each time we traverse matrix[j][i-j] or matrix[i-j][j] depends on which direction we go. 
Once we understand the description above, everything else is easy.

"""

class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        res = []
        M, N, flag = len(matrix), len(matrix[0]), True
        for i in range(0, M + N - 1):
            if flag == False:
                for j in range(max(i + 1 - N, 0), min(i + 1, M )):
                    res.append(matrix[j][i - j])
                flag = True
            else:
                for j in range(max(i + 1 - M, 0), min(i + 1, N )):
                    res.append(matrix[i - j][j])
                flag = False
        return res
