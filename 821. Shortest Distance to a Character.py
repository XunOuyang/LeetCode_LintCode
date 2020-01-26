class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        res = []
        index = -1
        for i, c in enumerate(S):
            if c == C and index < 0:
                count = i
                for j in range(index+1, i+1):
                    res.append(count)
                    count -= 1
                index = i
            elif c == C:
                count = i
                mid = (i+index)/2
                for j in range(index+1, i+1):
                    res.append(min(abs(j-index), abs(j-i)))
                index = i
            elif i == len(S)-1:
                for j in range(index+1, i+1):
                    res.append(j-index)
        return res
                
