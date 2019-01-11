# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 16:39:53 2018

@author: TZLMYQ
"""

class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        d = {i:set() for i in range(numCourses)}
        for courses in prerequisites:
            d[courses[1]].add(courses[0])
        visited = [False]*numCourses
        stack = []
        
        def topologicalSort(v, visited, stack):
            visited[v] = True
            for i in d[v]:
                if visited[i] == False:
                    topologicalSort(i, visited, stack)
            stack.append(v)
        
        for i in range(numCourses):
            if visited[i] == False:
                topologicalSort(i, visited, stack)
        return stack
    
    
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
        
solution = Solution()
print(solution.findOrder(numCourses, prerequisites))
        
        

