"""
Freewheel 当年的面试题，也是一道经典题。

"""
class Solution:
    def wordBreak(self, s: str, words: List[str]) -> bool:
        words = set(words)
        if not s or s in words:
            return True
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(len(s)):
            for j in range(i, len(s) + 1):
                if dp[i] and s[i:j] in words:
                    dp[j] = True
        return dp[-1]
