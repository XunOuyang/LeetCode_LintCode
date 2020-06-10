class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x:len(x))
        res = 0
        d = dict()
        for word in words:
            for i in range(len(word)):
                d[word] = max(d.get(word, 1), d.get(word[:i] + word[i+1:], 0) + 1)
                res = max(res, d[word])
        return res
