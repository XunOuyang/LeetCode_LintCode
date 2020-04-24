class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(reverse=True)
        while intervals:
            interval = intervals.pop()
            [left, right] = interval
            while intervals:
                if intervals[-1][0] <= right:
                    right = max(right, intervals[-1][1])
                    intervals.pop() 
                else:
                    break
            res.append([left, right])
        return res
