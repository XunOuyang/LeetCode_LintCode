# 这道题有几个值得注意的地方。
# 1. 需要用priority queue！
# 2. 先比较ladder，然后再计算bricks的逻辑
# 3. 循环里面用i 跟 i + 1比较，而不要用i 跟i - 1比较

import Queue
class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        """
        :type heights: List[int]
        :type bricks: int
        :type ladders: int
        :rtype: int
        """
        q = Queue.PriorityQueue()
        for i in range(len(heights) - 1):
            if heights[i + 1] > heights[i]:
                q.put(heights[i + 1] - heights[i])
            if q.qsize() > ladders:
                bricks -= q.get()
            if bricks < 0:
                return i           
        return len(heights) - 1
