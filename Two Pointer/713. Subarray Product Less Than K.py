class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        left = 0
        res = 0
        temp = 1
        for i in range(len(nums)):
            temp *= nums[i]
            while temp >= k:
                temp /= nums[left]
                left += 1
            res += i - left + 1
        return res
            
