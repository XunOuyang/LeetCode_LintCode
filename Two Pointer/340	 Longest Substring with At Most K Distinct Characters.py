class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):
        # write your code here
        if not s:
            return 0
        elif len(set(s)) <= k:
            return len(s)
        visited = set()
        q = collections.deque()
        res = 0
        d = dict()
        for c in s:
            if c not in visited:
                visited.add(c)
                d[c] = 1
                q.append(c)
                while len(visited) > k:
                    letter = q.popleft()
                    d[letter] -= 1
                    if d[letter] == 0:
                        visited.remove(letter)
            else:
                q.append(c)
                d[c] += 1
            res = max(res, len(q))
        return res
        
