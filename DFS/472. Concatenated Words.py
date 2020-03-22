"""
Two different solution. But figuring out the time complexity and space complexity are not easy.
Check https://www.youtube.com/watch?v=QGVCnjXmrNg   to get more details

"""

class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        wordDict = set(words)
        cache = {}
        return [word for word in words if self.check(word, wordDict, cache)]
    
    def check(self, word, wordDict, cache):
        if word in cache:
            return cache[word]
        for i in range(1, len(word)):
            if word[:i] in wordDict:
                if word[i:] in wordDict or self.check(word[i:], wordDict, cache):
                    cache[word] = True
                    return True
        cache[word] = False
        return False
        
        """
        res = []
        container = set(words)
        for word in words:
            container.remove(word)
            if self.check(word, container):
                res.append(word)
            container.add(word)
        return res
    
    def check(self, word, container):
        if word in container:
            return True
        for i in range(1, len(word)):
            if word[:i] in container and self.check(word[i:], container):
                return True
        return False
        """
