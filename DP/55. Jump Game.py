class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2:
            return True
        left = 0
        right = nums[0]
        while right < len(nums)-1:
            temp = right
            if left == right:
                return False
            for i in range(left, right+1):
                temp = max(temp, i+nums[i])
            left = right
            right = temp
        return True
