"""
Same problem as 493, and there are multiple solutions to it.
"""


class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        res = []
        while nums:
            num = nums.pop()
            index = bisect.bisect_left(stack, num)
            res.append(index)
            bisect.insort(stack, num)
        return res[::-1]
        
        
