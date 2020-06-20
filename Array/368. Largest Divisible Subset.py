class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        nums.sort()
        res = [[num] for num in nums]
        for i in range(len(nums)):
            temp = [nums[i]]
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(res[j]) >= len(res[i]):
                    res[i] = res[j] + [nums[i]]
        return max(res, key=len)
