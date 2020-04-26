class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        d = collections.defaultdict(list)
        for i, c in enumerate(S):
            d[c].append(i)
        stack = []
        res = []
        visited = set()
        for i in range(len(S)):
            if S[i] not in visited:
                left_most, right_most = float('inf'), float('-inf')
                stack = [i]
                visited.add(S[i])
                while stack:
                    num = stack.pop()
                    left, right = d[S[num]][0], d[S[num]][-1]
                    left_most = min(left, left_most)
                    right_most = max(right, right_most)
                    visited.add(S[num])
                    for j in range(d[S[num]][0] + 1, d[S[num]][-1]):
                        if S[j] not in visited:
                            stack.append(j)
                            visited.add(S[j])
                res.append(right_most - left_most + 1)
            stack = []
        return res
