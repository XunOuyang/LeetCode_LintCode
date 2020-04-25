"""
这种题真的没啥技巧。题目也不差，但是搞不清考察的是什么
"""
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if collections.Counter(pushed) != collections.Counter(popped):
            return False
        stack = []
        left = 0
        for num in pushed:
            if num != popped[left]:
                stack.append(num)
            else:
                left += 1
            while stack and stack[-1] == popped[left]:
                stack.pop()
                left += 1
        if left == len(popped) and not stack:
            return True
        return False
