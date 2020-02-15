# A very non-typical problem which looks for a special point which split the array into 
# 2 parts, first part of the array will all add K and the second part will all minus K.
class Solution(object):
    def smallestRangeII(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A.sort()
        bottom, top = A[0], A[-1]
        res = top - bottom
        for i in range(1, len(A)):
            res = min(res, max(top-K, A[i-1]+K)-min(bottom+K, A[i]-K))
        return res
