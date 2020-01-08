"""
This is a pretty easy question. Just be careful that the question request candidate to 
check if the arr can reach any 0 or not. Reaching all the 0s is not required.
It can be done by BFS too.
"""

class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        if arr[start] == 0:
            return True
        stack = [start]
        visited = set()
        while stack:
            origin = stack.pop()
            visited.add(origin)
            left, right = origin-arr[origin], origin+arr[origin]
            if left >= 0 and left not in visited:
                if arr[left] == 0:
                    return True
                stack.append(left)
                visited.add(left)
            if right < len(arr) and right not in visited:
                if arr[right] == 0:
                    return True
                stack.append(right)
                visited.add(right)
        return False
      
                    
                    
