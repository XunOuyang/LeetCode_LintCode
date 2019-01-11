# -*- coding: utf-8 -*-
"""
Created on Thu May 10 08:45:30 2018

@author: tzlmyq
"""
import collections
class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if matrix == [] or matrix == [[]]:
            return matrix
        M, N = len(matrix), len(matrix[0])
        matrix_new = [[0 for i in range(N)] for j in range(M)]
        def neighbor(i, j):
            for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= x < M and 0 <= y < N:
                    yield x, y        
        q = collections.deque( [((x, y), 0) for x in range(M) for y in range(N) if matrix[x][y] == 0])
        visited = set((element for (element, _) in q))
        while q:
            (x, y), depth = q.popleft()
            matrix_new[x][y] = depth
            for nei in neighbor(x, y):
                if nei not in visited:
                    visited.add(nei)
                    q.append((nei, depth + 1))
        return matrix_new
    
    
solution = Solution()
matrix = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
print solution.updateMatrix(matrix)