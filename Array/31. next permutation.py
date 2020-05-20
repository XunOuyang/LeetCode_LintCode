class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return nums
        if nums == sorted(nums, reverse=True):
            return nums.sort()
        i = len(nums) - 1
        while i > 0:
            if nums[i-1] < nums[i]:
                break
            i -= 1
        for j in range(len(nums)-1, -1, -1):
            if nums[j] > nums[i-1]:
                nums[j], nums[i-1] = nums[i-1], nums[j]
                break
        left, right = i, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
