"""
Same problem as 315, multiple solutions to it
"""

class Solution(object):
    def reversePairs(self, nums):
        stack = []
        res = 0
        while nums:
            num = nums.pop()
            index = bisect.bisect_left(stack, num/2.0)
            res += index
            bisect.insort(stack, num)
        return res
