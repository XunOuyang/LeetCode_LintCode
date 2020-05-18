class Solution:
    def checkInclusion(self, p: str, s: str) -> bool:
        counter_p = collections.Counter(p)
        counter = dict()
        size = 0
        q = collections.deque()
        for i, c in enumerate(s):
            if c in counter_p:
                counter[c] = counter.get(c, 0) + 1
                size += 1
                q.append(i)
                while counter[c] > counter_p[c]:
                    temp = q.popleft()
                    counter[s[temp]] -= 1
                    size -= 1
                if size == len(p):
                    return True
            else:
                while q:
                    temp = q.popleft()
                    counter[s[temp]] -= 1
                    size -= 1
        return False
