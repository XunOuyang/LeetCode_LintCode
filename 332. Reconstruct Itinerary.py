# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 20:07:42 2018

@author: TZLMYQ
"""
import collections
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        self.d = collections.defaultdict(list)
        for ticket in tickets:
            self.d[ticket[0]] += [ticket[1]]
        print(self.d)
        self.res = []
        self.dfs(0, "JFK", [],  tickets)
        self.res.sort()
        print(self.res)
  #      return self.res[0]
    
    def dfs(self, index, start, path, tickets):
        path += [start]
        print(path)
        if len(path) == len(tickets)+1:
            self.res.append(path)
            return
        elif self.d[start] == []:
            return
        for i in range(index,  len(self.d[start])):
            self.dfs(index+1, self.d[start][i] , path,  tickets)
        
    
solution = Solution()
#tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
print(solution.findItinerary(tickets))