"""
This problem is an follow up of 334 annd 200.
"""
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes:
            return 0
        envelopes.sort(key=lambda x:x[1])
        dp = [1 for i in range(len(envelopes))]
        for i in range(len(envelopes)):
            left, right = i+1, len(envelopes)-1
            while left < right:
                mid = (left+right)/2
                if envelopes[i][0] >= envelopes[mid][0] and envelopes[i][1] >= envelopes[mid][1]:
                    left = mid + 1
                else:
                    right = mid
                    dp[j] = max(dp[j], dp[i]+1)
        return max(dp)
        
