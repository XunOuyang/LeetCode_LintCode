class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        counter_p = collections.Counter(p)
        counter = dict()
        size = 0
        q = collections.deque()
        res = []
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
                    res.append(q[0])
            else:
                while q:
                    temp = q.popleft()
                    counter[s[temp]] -= 1
                    size -= 1
        return res
