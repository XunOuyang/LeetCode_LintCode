"""
这是一道非常有意思的题目，有意思的地方在哪里呢？其实两个的写法差不多。解法1就是纯粹的recursion，但是解法1是dynamic programming。
这个解法2呢，就是比较标准的dynamic programming的解法了，如果用C++解这道题也是一样的。但是其实并不够pythonic。
所以就有了解法3，详细关于@lru_cache()的用法在这里，https://docs.python.org/3.3/library/functools.html
但是其实也不应该由于不知道这个用法而无法解出来这道题。
"""

class NotAccepetedSolution1:
    def minDays(self, n: int) -> int:
        if n <= 1:
            return n
        return 1 + min(self.minDays(n // 2) + n % 2, self.minDays(n // 3) + n % 3)

class Solution2:
    def __init__(self):
        self.dp = dict()
    def minDays(self, n: int) -> int:
        if n <= 1:
            return n
        if n not in self.dp:
            self.dp[n] = 1 + min(self.minDays(n // 2) + n % 2, self.minDays(n // 3) + n % 3)
        return self.dp[n]
        
class Solution3:
    def minDays(self, n: int) -> int:
        @lru_cache(None)
        def helper(x):
            if x <= 1:
                return 1
            return 1 + min(helper(n // 2) + n % 2, helper(n // 3) + n % 3)
        return helper(n)
