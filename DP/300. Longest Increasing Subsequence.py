# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 20:27:42 2018

@author: TZLMYQ
Solution3的写法更加节约空间。这个dp的问题跟往常的dp问题不太一样，longest increasing subsequence属于新的典型的一类题。
往简单了看，用O（n）的空间复杂度加上O（n^2）的时间复杂度，很容易的两个for 循环dp就能做。比如solution2.
但是要做到O（nlogn）的时间复杂度，以及O（k）的空间复杂度，solution3才是最好的。结合了二分法。
"""

class Solution(object):
    def lengthOfLIS(self, nums):
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            i, j = 0, size
            while i != j:
                m = (i + j) / 2
                if tails[m] < x:
                    i = m + 1
                else:
                    j = m
            tails[i] = x
            size = max(i + 1, size)
        return size
    
class Solution2(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        temp = 0 
        DP = [1]*(len(nums))
        for i in xrange(1,len(nums)):
            for j in xrange(i):
                if nums[i]>nums[j]:
                    DP[i] = max(DP[i],DP[j]+1)                    
        return max(DP)
    
solution = Solution()
nums = [-10, -3, -2, -9] 
print solution.lengthOfLIS(nums)


class Solution3(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > dp[-1]:
                dp.append(nums[i])
            else:
                index = bisect.bisect_left(dp, nums[i])
                dp[index] = nums[i]
        return len(dp)
