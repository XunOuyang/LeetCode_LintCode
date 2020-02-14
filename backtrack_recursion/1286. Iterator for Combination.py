class CombinationIterator(object):

    def __init__(self, characters, combinationLength):
        """
        :type characters: str
        :type combinationLength: int
        """
        self.res = []
        self.recursion(characters, combinationLength, 0, "")
        self.counter = 0
        
    def recursion(self, s, k, index, path):
        if len(path) == k:
            self.res.append(path)
            return
        for i in range(index, len(s)):
            self.recursion(s, k, i+1, path+s[i])

    def next(self):
        """
        :rtype: str
        """
        if self.hasNext():
            val = self.res[self.counter]
            self.counter += 1
            return val
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.counter < len(self.res):
            return True
        return False


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
