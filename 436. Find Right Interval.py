# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 10:26:25 2018

@author: tzlmyq
"""
import bisect

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        if not intervals or len(intervals) < 2:
            return [-1]
        intervals = [[intervals[i].start, intervals[i].end, i] for i in range(len(intervals))]
        intervals.sort()
        print intervals
        res = [None] * len(intervals)
        start_time = [interval[0] for interval in intervals]
        for interval in intervals:
            position = bisect.bisect_left(start_time, interval[1])
      #      print interval[1]
            if position == len(intervals):
                res[interval[2]] = -1
                
            else:
                res[interval[2]] = intervals[position][2]
       #     print res
        return res
        
    
intervals = []
intervals.append(Interval(3,4))
intervals.append(Interval(2,3))
intervals.append(Interval(1,2))

    
solution = Solution()
print solution.findRightInterval(intervals)
