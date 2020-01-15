class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        res = 0
        d = {0:1}
        s = 0
        for a in A:
            s += a
            res += d.get(s%K, 0)
            d[s%K] = d.get(s%K, 0) + 1
        return res
