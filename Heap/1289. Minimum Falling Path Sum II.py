import heapq
class Solution(object):
    def minFallingPathSum(self, arr):
        """
        :type arr: List[List[int]]
        :rtype: int
        """
        for i in range(len(arr)-1):
            a = heapq.nsmallest(2, [[val, pos] for pos, val in enumerate(arr[i])])
            print(a)
            for j in range(len(arr[0])):
                arr[i+1][j] += a[0][0] if j!= a[0][1] else a[1][0]
        return min(arr[-1])
                
 """
 For this problem, be careful to record the position of smallest elements. There could be multiple smallest elements
 at different columnn within the same row. 
 
 """
