class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        count = 1
        left = 0
        right = nums[0]
        while right < len(nums)-1:
            temp = right
            for i in range(left, right+1):
                temp = max(temp, i+nums[i])
            left = right
            right = temp
            count += 1
        return count
