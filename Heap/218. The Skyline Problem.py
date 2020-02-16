from Queue import PriorityQueue
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        """
        we use heap to store the key points of the building.
        [negtiveHeight, pos]
        for each iteration, we go through all the key points(corner points)
        if the new key points height will be added to the heap.
        if the current largest(stored in heap) is different than the previous one, then it will be added to the result.
        """
        res = [[-1, 0]]
        q = PriorityQueue()
        heights = []
        for building in buildings:
            heights.append([building[0], -building[2], building[1]])
            heights.append([building[1], 0, 0])
        heights.sort()
        hp = [[0, float("inf")]]
        for height in heights:
            [x, y, z] = height
            while x >= hp[0][1]:
                heapq.heappop(hp)
            if y:
                heapq.heappush(hp, [y, z])
            if res[-1][-1] != -hp[0][0]:
                res.append([x, -hp[0][0]])
        return res[1:]
        
        
