class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        # write your code here
        left, right = 0, 0
        while right < len(nums):
            if nums[left] == 0:
                while right < len(nums) and nums[right] == 0:
                    right += 1
                if right < len(nums):
                    nums[left], nums[right] = nums[right], nums[left]
            else:
                left += 1
                right = max(right, left)
        
                    
