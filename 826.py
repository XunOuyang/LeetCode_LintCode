# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 22:48:53 2018

@author: tzlmyq
"""
import bisect
class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        res = 0
        new_list = [list(i) for i in zip(difficulty, profit)]
        new_list.sort()
        temp = new_list[0][1]
    
        for i in range(len(new_list)):
            new_list[i][1] = max(new_list[i][1], temp)
            temp = new_list[i][1]
        profit = map(lambda x : x[1], new_list)
        difficulty = map(lambda x : x[0], new_list)
        for i in range(len(worker)):
            index = bisect.bisect_right(difficulty, worker[i])
            if index > 0:
                res += new_list[index-1][1]
        return res
    
a = Solution()
difficulty = [68,35,52,47,86]
profit = [67,17,1,81,3]
worker = [92,10,85,84,82]


print a.maxProfitAssignment( difficulty, profit, worker)