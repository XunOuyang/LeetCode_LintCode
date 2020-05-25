class Solution:
    def findLengthOfLCIS(self, A: List[int]) -> int:
        # write your code here
        if not A:
            return 0
        res = 1
        temp = 1
        for i in range(1, len(A)):
            if A[i] > A[i-1]:
                temp += 1
            else:
                temp = 1
            res = max(res, temp)
        return res
