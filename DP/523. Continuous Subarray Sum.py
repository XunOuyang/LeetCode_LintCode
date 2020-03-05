class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k == 0:
            return any(nums[i] == 0 and nums[i + 1] == 0 for i in range(len(nums) - 1))
        d, s = {0: -1}, 0
        for i, num in enumerate(nums):
            s = (s + num) % k
            if s in d and i - d[s] > 1:
                return True
            if s not in d:
                d[s] = i
        return False
