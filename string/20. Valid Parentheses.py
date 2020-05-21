class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        if len(s) % 2:
            return False
        stack = []
        for c in s:
            if c in {"(", "[", "{"}:
                stack.append(c)
            elif c == ")":
                if not stack or stack[-1] != "(":
                    return False
                else:
                    stack.pop()
            elif c == "]":
                if not stack or stack[-1] != "[":
                    return False
                else:
                    stack.pop()
            elif c == "}":
                if not stack or stack[-1] != "{":
                    return False
                else:
                    stack.pop()
        return not stack
