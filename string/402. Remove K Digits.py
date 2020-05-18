class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        i = 0
        stack = []
        while i < len(num):
            while stack and k and stack[-1] > num[i]:
                stack.pop()
                k -= 1
            stack.append(num[i])
            i += 1
        while k:
            stack.pop()
            k -= 1
        i = 0
        while i < len(stack) and stack[i] == '0':
            i += 1
        stack = stack[i:]
        if not stack:
            return "0"
        return "".join(stack)
        
        
