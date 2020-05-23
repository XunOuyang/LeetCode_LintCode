class Solution:
    def frequencySort(self, s: str) -> str:
        counter = collections.Counter(s)
        res = ""
        for item in sorted(counter.items(), key=lambda x:x[1], reverse=True):
            res += item[0] * counter[item[0]]
        return res
