# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 11:01:04 2018

@author: tzlmyq
"""

"""
Solution 1 : use a set to store all the values it can reach. and keep updating the set while it traverse all the 
elements in nums. Be carefule about the set. and the initial value of set should be 0.
"""
class Solution1(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums or len(nums) <2:
            return False
        total = sum(nums)
        if total%2 == 1:
            return False
        nums.sort()
        total = total / 2
        if nums[-1] > total:
            return False
        s= set([0])
        for num in nums:
            new_list = []
            for i in s:
                if num + i == total:
                    return True
                else:
                    new_list.append(num + i)
            s.update(new_list)        
        return False
    
"""
Solution 2: DP. be very careful about deep copy of the list.
"""
    
class Solution2(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums or len(nums) <2:
            return False
        total = sum(nums)
        if total%2 == 1:
            return False
        nums.sort()
        total = total / 2
        if nums[-1] > total:
            return False
        dp = [False for _ in xrange(total+1)]
        dp[0] = True
        for num in nums:
            new_dp = dp[:]
            for i in xrange(total+1):
                if new_dp[i] and i + num <= total:
                    dp[i+num] = True                
        return dp[-1]
    
    
