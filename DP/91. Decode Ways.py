"""
https://leetcode.com/problems/decode-ways/discuss/253018/Python%3A-Easy-to-understand-explanation-bottom-up-dynamic-programming
本题解法来自于以上链接。这道题很灵活。
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, len(s) + 1): 
            if s[i-1:i] > '0':
                dp[i] += dp[i-1]
            if i and 9 < int(s[i-2:i]) < 27:
                dp[i] += dp[i-2]
        return dp[-1]
