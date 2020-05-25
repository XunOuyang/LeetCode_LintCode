class Solution:
    def getColumn(self, arr):
        # Write your code here
        if not arr:
            return -1
        pointer = len(arr[0]) - 1
        for row in arr:
            while pointer >= 0 and row[pointer] == 1:
                pointer -= 1
        return pointer + 1
