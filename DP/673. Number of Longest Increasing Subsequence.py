# 这应该是一道思路特别清晰的题目
# 1. 我们需要构建两个数组来记录，dp 和 count，dp[i]表示到i 为止，最长的递增子序列有多长，count[i]表示，到i为止，递增的子序列有多少个。
# 2. 那么根据上面的定义，就不难得到更新他们的方法了。
class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        max_length = 1
        dp = [1] * len(nums)
        res = 1
        count = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] >= nums[i]:
                    continue
                if dp[j] + 1 == dp[i]:
                    count[i] += count[j]
                elif dp[j] + 1 > dp[i]:
                    count[i] = count[j]
                    dp[i] = dp[j] + 1
            if max_length == dp[i]:
                res += count[i]
            elif max_length < dp[i]:
                res = count[i]
                max_length = dp[i]
        return res
