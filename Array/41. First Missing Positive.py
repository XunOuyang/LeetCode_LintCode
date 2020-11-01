# 千万要注意，python 里面，for 循环不会改变nums 的值，所以第10行一定要用while。

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if nums[i] > len(nums) or nums[i] <= 0:
                nums[i] = 0
            while nums[i] != i + 1 and 0 < nums[i] <= len(nums) and nums[nums[i] - 1] != nums[i]:
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]
            i += 1
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1
