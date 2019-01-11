# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 09:53:17 2018

@author: tzlmyq
"""

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        res = [1]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                res.append(res[-1]+1)
            else:
                res.append(1)
                
        for i in range(len(ratings)-1, 0, -1):
            if ratings[i-1] > ratings[i]:
                res[i-1] = max(res[i]+1, res[i-1])
        return sum(res)
        
    
solution = Solution()
ratings = [1,3,4,5,2]
print solution.candy(ratings)