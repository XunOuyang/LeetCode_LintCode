# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 00:10:05 2018

@author: TZLMYQ
"""
import collections
class Solution(object):
    def canFinish(self, num, courses):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        d = collections.defaultdict(list)
        for i, j in courses:
            d[i].append(j)
            
        visited = [0]* num
        # if dfs return False, means there is a cycle
        def dfs(m):
            print m, len(visited)
            if visited[m] == -1:
                return False
            if visited[m] == 1:
                return True
            visited[m] = -1
            for n in d[m]:                
                if not dfs(n):
                    return False
            visited[m] = 1      
            return True
        
        for i in range(len(courses)):
            for j in d[i]:
                if not dfs(j):
                    return False
        return True
        
        
solution = Solution()
num = 2
courses = [[0, 1], [1, 0]] 
print(solution.canFinish(num, courses))