# 一道看起来代码只有几行，但是实际上却需要用数学去证明贪心的方向的题目。其实并不那么容易
class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        res = 0
        while Y != X:
            if Y > X:
                if Y % 2:
                    Y += 1
                else:
                    Y /= 2
            else:
                return int(res + X - Y)      
            res += 1
        return res
