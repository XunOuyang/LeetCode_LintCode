class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if not coordinates or len(coordinates) < 2:
            return False
        for i in range(2, len(coordinates)):
            [x1, y1], [x2, y2], [x3, y3] = coordinates[i], coordinates[i-1], coordinates[i-2]
            if (x1*y2 - x1*y3 + x2*y3 - x2*y1 + x3*y1 - x3*y2) != 0:
                print(i)
                return False
        return True
