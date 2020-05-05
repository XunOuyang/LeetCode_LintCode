class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        if H == len(piles):
            return max(piles)
        left, right = 0, max(piles) + 1
        while left != right - 1:
            mid = (left + right) // 2
            temp = 0
            for pile in piles:
                temp += ceil(pile / mid)
            if temp <= H:
                right = mid
            else:
                left = mid
        return right
        
