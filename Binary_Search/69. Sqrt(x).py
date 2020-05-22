class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = -1, x + 1
        while left != right  - 1:
            mid = (left + right) // 2
            if mid * mid > x:
                right = mid
            else:
                left = mid
        return left
