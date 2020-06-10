"""

"""
class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        dp = [0] * (len(s) + 1)
        dp[-1] = 1
        temp = ""
        for i in range(len(s)-1, -1, -1):
            if s[i] == '0':
                continue
            n = 0
            for j in range(1, len(s)-i+1):
                n = n * 10 + ord(s[i+j-1]) - ord('0')
                if n > k:
                    break
                dp[i] += dp[i+j]
            dp[i] = dp[i] % (10**9+7)
        return dp[0]
    
