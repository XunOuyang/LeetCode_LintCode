class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        """
        if we get a "(":
            pointer -= 1
        else:
            pointer += 1
        """
        left, right = 0, 0
        for s in S:
            if s == "(":
                left += 1
            elif left > 0:
                left -= 1
            else:
                right += 1
        return left + right
        
        """
        stack = []
        for s in S:
            if stack and stack[-1] == "(" and s == ")":
                stack.pop()
            else:
                stack.append(s)
        return len(stack)
        """
            
        
