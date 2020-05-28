class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = -n
        elif n == 0:
            return 1
        res = 1
        while n:
            temp = x
            p = 1
            while 2 * p <= n:
                p *= 2
                temp *= temp
            n -= p
            res *= temp
        return res
