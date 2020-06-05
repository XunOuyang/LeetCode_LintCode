class Solution:

    def __init__(self, w: List[int]):
        self.data = []
        self.limit = sum(w)
        self.acc = 0
        for i, item in enumerate(w):
            self.acc += item
            self.data.append(self.acc/self.limit)

    def pickIndex(self) -> int:
        pos = bisect.bisect_left(self.data, random.random())
        return pos
        
