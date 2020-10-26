class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        left, right = matrix[0][0] - 1, matrix[-1][-1] + 1
        while left != right - 1:
            mid = (left + right) // 2
            temp = 0
            for i in range(len(matrix)):
                pos = bisect.bisect_right(matrix[i], mid)
                temp += pos
            if temp >= k:
                right = mid
            else:
                left = mid
        return right
