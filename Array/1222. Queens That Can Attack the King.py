class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        res = []
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        for direction in directions:
            k = 1
            while 0 <= king[0] + k * direction[0] < 9 and 0 <= king[1] + k * direction[1] < 9:
                pos = [king[0] + k * direction[0], king[1] + k * direction[1]]
                if pos in queens:
                    res.append(pos)
                    break
                else:
                    k += 1
        return res
