class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res, min_prod, max_prod = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            min_prod, max_prod = min(min_prod * nums[i], max_prod * nums[i], nums[i]), max(min_prod * nums[i], max_prod * nums[i], nums[i])
            res = max(res, max_prod)
        return res
                    
