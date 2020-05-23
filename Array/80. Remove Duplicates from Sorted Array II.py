"""
这道题一点也不容易

"""

class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, nums):
        # write your code here
        res = 0
        for n in nums:
            if res < 2 or n > nums[res-2]:
                nums[res] = n
                res += 1
        return res
            
