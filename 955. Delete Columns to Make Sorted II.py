class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        res = 0
        if not A:
            return res
        flag = [False] * len(A)
        for i in range(len(A[0])):
            j = 0
            while j < len(A)-1:                
                if not flag[j] and A[j][i] > A[j+1][i]:
                    res += 1
                    break                    
                j += 1
            if j < len(A) - 1:
                continue
            for j in range(len(A) - 1):
                flag[j] = flag[j] or A[j][i] < A[j+1][i]               
                
        return res
