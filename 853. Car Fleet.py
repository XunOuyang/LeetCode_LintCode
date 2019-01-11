# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 16:27:23 2018

@author: tzlmyq
"""

class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        if not position or not speed:
            return 0
        status = []
        for i in range(len(position)):
            status.append([position[i], speed[i]])
        status.sort()
        res = 1
        print status
        while status:
            p, s = status.pop()
            if status:
                if s >= status[-1][1]:
                    res += 1
                elif float(target - p)/s < float(p - status[-1][0])/(status[-1][-1] - s):
                    res += 1
                else:
                    status[-1][-1] = s
                    status[-1][0] = p
        return res
        
solution = Solution()
target = 13
position = [10,2,5,7,4,6,11]
speed = [7,5,10,5,9,4,1]
print solution.carFleet(target, position, speed)