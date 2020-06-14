import queue
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        elif m * k == len(bloomDay):
            return max(bloomDay)
        left, right = min(bloomDay) - 1, max(bloomDay) + 1
        if left >= right - 1:
            return right
        while left != right - 1:
            mid = (left + right) // 2
            count = 0
            temp_k = k
            temp_m = m
            for i, num in enumerate(bloomDay):
                if num <= mid:
                    temp_k -= 1
                    if temp_k == 0:
                        temp_m -= 1
                        temp_k = k
                else:
                    temp_k = k
                if temp_m <= 0:
                    break
            if temp_m <= 0:
                right = mid
            else:
                left = mid
        return right
