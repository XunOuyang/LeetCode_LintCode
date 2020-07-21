"""
这道题看起来甚至都没有什么特别的。但是千万要注意，从第8行到14行，就是一个非常好的优化思路，可以让整个程序速度变得稍快。
而第32行的break，则是整个程序的关键，如果没有这个break，整个程序时间复杂度将上升一个维度。
"""

class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        A_chars, B_chars = [], []
        for a, b in zip(A, B):
            if a != b:
                A_chars.append(a)
                B_chars.append(b)
        A = "".join(A_chars)
        B = "".join(B_chars)
        visited = set(B)
        stack = [A]
        res = 0
        while stack:
            new_stack = []
            while stack:
                string = stack.pop()
                if string == B:
                    return res
                for i in range(len(B)):
                    if string[i] != B[i]:
                        for j in range(i + 1, len(B)):
                            if string[j] != B[j] and string[j] == B[i]:
                                new_string = string[:i] + string[j] + string[i+1:j] + string[i] + string[j+1:]
                                if new_string not in visited:
                                    visited.add(new_string)
                                    new_stack.append(new_string)
                        break
            stack = new_stack   
            res += 1
        return -1
