class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0
        points.sort(key=lambda x:x[1])
        right = points[0][1]
        res = 1
        for i in range(1, len(points)):
            if points[i][0] > right:
                right = points[i][1]
                res += 1
        return res
            
