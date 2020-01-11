class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        dp = [1] + [0]*target
        for i in range(target+1):
            for num in nums:
                if num > i:
                    break
                else:
                    dp[i] += dp[i-num]
        return dp[target]
