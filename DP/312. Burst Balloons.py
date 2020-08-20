class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        Thoughts:
            1. First we need to add [1] to the left of the nums and [1] to the right of the nums.
            2. We have to define range of the length: 1<= length <= n
            3. We have to define the range of i: this is difficult, first we know 1<= i
            4. We know the relationship between i and j:  j = i + length - 1, and we know j <= n which makes j < n+1 which makes i+length - 1 < n+1 which makes i < n + 2 - length
            5. We know the range of k: i<= k <= j
            6. The most difficult part, formular!
        Similar problem:
            1457
        """
        n = len(nums)
        nums = [1]+nums+[1]
        dp = [[0 for i in range(n+2)] for j in range(n+2)]
        
        for length in range(1, n+1):
            for i in range(1, n+2-length):
                j = i+length-1
                for k in range(i, j+1):
                    dp[i][j] = max(dp[i][j], dp[i][k-1]+nums[i-1]*nums[k]*nums[j+1]+dp[k+1][j])
        return dp[1][n]
                    
