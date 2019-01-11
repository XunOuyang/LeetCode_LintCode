# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 16:02:46 2018

@author: TZLMYQ
"""

class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        courses.sort(key=lambda x:x[1])
        """
        dp = [[0,0]*len(courses)]
        for i in range(len(courses)):
            for j in range(len(courses)):
        """
        dp = [0 for i in range((len(courses)))]
        dp[0] = 1
        for i in range(1, len(courses)):
            if courses[i][0] >= courses[i-1][1]:
                dp[i] = max(dp[i-1]+1, dp[i])
            else:
                dp[i] = max(dp[i-1], dp[i])
                courses[i][1] = courses[i-1][1]
  #      print courses, dp
        return dp[-1]
    
solution = Solution()
courses = [[100, 200], [200, 1300], [1000, 1250], [1240,2100], [1300, 2000],[1250, 1900],  [2000, 3200]]
print(solution.scheduleCourse(courses))
                