import queue
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        q = queue.PriorityQueue()
        for point in points:
            q.put([point[0]**2+point[1]**2, point[0], point[1]])
        res = []
        while K:
            K -= 1
            _, x, y = q.get()
            res.append([x, y])
        return res
