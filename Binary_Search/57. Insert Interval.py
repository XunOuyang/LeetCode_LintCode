class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        [left, right] = newInterval
        lefts = [interval[0] for interval in intervals]
        rights = [interval[1] for interval in intervals]
        left_index = bisect.bisect_left(lefts, left)
        right_index = bisect.bisect_right(rights, right)
        if left_index > 0:
            if left <= intervals[left_index-1][1]:
                left_index -= 1
                left = intervals[left_index][0]
        if right_index < len(intervals):
            if right >= intervals[right_index][0]:
                right = intervals[right_index][1]
            else:
                right_index -= 1
        intervals[left_index:right_index+1] = [[left, right]]
        return intervals
