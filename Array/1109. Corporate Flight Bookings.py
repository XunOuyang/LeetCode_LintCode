"""
It is like a super simplified skyline problem. You first memorize initial weight to the list, then reduce the weight when it is done.
"""

class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        res = [0 for i in range(n+1)]
        for booking in bookings:
            res[booking[0]-1] += booking[2]
            res[booking[1]] -= booking[2]
        for i in range(1, len(res)):
            res[i] += res[i-1]
        res.pop()
        return res
