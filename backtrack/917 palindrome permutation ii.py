"""
This problem is leetcode 47 follow up problem. It only needs to preprocess some data 
to get the problem turns to permutation ii.
"""

class Solution:
    """
    @param s: the given string
    @return: all the palindromic permutations (without duplicates) of it
    """
    def generatePalindromes(self, s):
        # write your code here
        counter = collections.Counter(s)
        odd = 0
        mid = ""
        elements = []
        for item in counter:
            if counter[item]%2:
                mid = item
                odd += 1
            for i in range(counter[item]/2):
                elements.append(item)
        
        if odd > 1:
            return []
        permutations = self.permute(elements)
        res = []
        for item in permutations:
            item = "".join(item)
            res.append(item+mid+item[::-1])
        return res
        
    def permute(self, elements):
        res = []
        elements.sort()
        visited = [False]*len(elements)
        self.backtrack(elements, [], res, visited)
        return res
        
    def backtrack(self, elements, path, res, visited):
        if(len(path)==len(elements)):
            res.append(path)
        for i in range(len(elements)):
            if not visited[i]:
                if i > 0 and elements[i] == elements[i-1] and not visited[i-1]:
                    continue
                visited[i] = True
                self.backtrack(elements, path+[elements[i]], res, visited)
                visited[i] = False
            
        
            
    
