class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1] * len(nums)
        temp = 1
        for i in range(len(nums)-1):
            temp *= nums[i]
            res[i+1] *= temp
        temp = 1
        for i in range(len(nums)-1, 0, -1):
            temp *= nums[i]
            res[i-1] *= temp
        return res
            
