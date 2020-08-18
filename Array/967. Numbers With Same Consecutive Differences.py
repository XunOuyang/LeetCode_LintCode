class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        if N == 0:
            return []
        nums = [i for i in range(1, 10)]
        if N == 1:
            return [0] + nums
        for i in range(1, N):
            new_nums = []
            for num in nums:
                if num % 10 + K < 10:
                    new_nums.append(num * 10 + num % 10 + K)
                if num % 10- K >= 0 and K:
                    new_nums.append(num * 10 + num % 10 - K)
            nums = new_nums
        return nums
