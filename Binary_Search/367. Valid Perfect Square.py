class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num <= 0:
            return False
        left, right = 0, num + 1
        while left != right - 1:
            mid = (left + right) // 2
            if mid * mid == num:
                return True
            elif mid * mid < num and (mid + 1) ** 2 > num:
                return False
            elif mid ** 2 < num:
                left = mid
            else:
                right = mid
        return False
