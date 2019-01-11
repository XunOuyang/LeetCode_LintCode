ngyi # -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 10:11:55 2018

@author: tzlmyq
"""
"""
 Solution 1 is the most naive solution. though it solves problem.
 We could reduce the space complexity from O(m*n) to O(n) though.
"""
class Solution1(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False
        if not s1 or not s2:
            return s3 == s1 or s3 == s2
        dp = [[False for _ in range(len(s1)+1)] for _ in range(len(s2)+1)]
        dp[0][0] = True
        
        for i in range(1, len(s1)+1):            
            dp[0][i] = (s1[i-1] == s3[i-1])&dp[0][i-1]
        
        for j in range(1, len(s2)+1):
            dp[j][0] = (s2[j-1] == s3[j-1])&dp[j-1][0]
            
        for i in range(1, len(s1)+1):
            for j in range(1, len(s2)+1):
                dp[j][i] = (dp[j-1][i] & (s2[j-1]==s3[i+j-1])) or (dp[j][i-1] & (s1[i-1]==s3[i+j-1]))
        return dp[-1][-1]
    
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False
        if not s1 or not s2:
            return s3 == s1 or s3 == s2
        stack = [(0,0)]
        visited = set((0, 0))
        while stack:
            i, j = stack.pop()
            if i+j == len(s3):
                return True
            if i+1 <= len(s1) and s1[i] == s3[i+j] and (i+1, j) not in visited:
                stack.append((i+1, j))
                visited.add((i+1, j))
            if j+1 <= len(s2) and s2[j] == s3[i+j] and (i, j+1) not in visited:
                stack.append((i, j+1))
                visited.add((i, j+1))
        return False
            
    
a = Solution()
s1 = "aa"
s2 = "ab"
s3 = "abaa"
print(a.isInterleave(s1, s2, s3))

"""
 we could also use dfs or bfs solution to get it done.
 
"""