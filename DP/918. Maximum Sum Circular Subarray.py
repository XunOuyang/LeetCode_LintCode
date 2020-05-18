"""
这是一道非常好的但同时又不算难的DP题。为什么是DP，因为有状态转移方程，而且需要建立一个长度为len(A)的数组来记录数据。
但是，由于算法的优化，可以有更加节约空间的做法。
同时，也利用了环的性质。环状数组prefix sum最大和就是max( 链状数组prefix sum最大和, 数组所有值的和减去链状数组prefix sum最小和)
想明白这是为什么。
"""
class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        local_min, local_max, glo_min, glo_max = A[0], A[0], A[0], A[0]
        for i in range(1, len(A)):
            local_min = min(local_min + A[i], A[i])
            local_max = max(local_max + A[i], A[i])
            glo_min = min(local_min, glo_min)
            glo_max = max(local_max, glo_max)
        if sum(A) != glo_min:
            glo_max = max(glo_max, sum(A) - glo_min)
        return glo_max
            
