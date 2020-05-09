class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        counter_t = collections.Counter(t)
        counter_s = collections.Counter(s)
        for item in counter_t:
            if counter_t[item] > counter_s[item]:
                return ""
        d = dict()
        for c in t:
            d[c] = 0
        length = len(counter_t)
        count = 0
        res = s
        left = 0
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]] += 1
                if d[s[i]] == counter_t[s[i]]:
                    count += 1
            while count == length:
                if len(res) > len(s[left:i+1]):
                    res = s[left:i+1]
                if s[left] in d:
                    d[s[left]] -= 1
                    if d[s[left]] < counter_t[s[left]]:
                        count -= 1
                left += 1
        return res
