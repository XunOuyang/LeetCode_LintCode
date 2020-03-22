# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 20:07:42 2018

@author: TZLMYQ
"""
import collections
class Solution1(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        self.d = collections.defaultdict(list)
        res = []
        for ticket in tickets:
            self.d[ticket[0]].append(ticket[1])
        for key in self.d:
            self.d[key].sort(reverse=True)
        stack = ["JFK"]
        
        while stack:
            city = stack[-1]
            if len(self.d[city]) == 0:
                res.append(city)
                stack.pop()
            else:
                stack.append(self.d[city].pop())
        return res[::-1]
    
class Solution2:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.d = collections.defaultdict(list)
        for ticket in tickets:
            self.d[ticket[0]].append(ticket[1])
        for key in self.d:
            self.d[key].sort(reverse=True)
        self.res = []
        self.dfs("JFK", tickets)
        return self.res[::-1]
    
    def dfs(self, start, tickets):
        if start in self.d and len(self.d[start]) > 0:
            while len(self.d[start]) > 0:
                next_stop = self.d[start].pop()
                self.dfs(next_stop, tickets)
        self.res.append(start)
        
from collections import deque
class Solution3:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.d = collections.defaultdict(list)
        for flight in tickets:
            self.d[flight[0]].append(flight[1])
        self.route = ["JFK"]
        length = len(tickets)
        self.dfs("JFK", length)
        return self.route
    
    def dfs(self, start, k):
        if len(self.route) == k + 1:
            return self.route
        cities = sorted(self.d[start])
        for city in cities:
            self.d[start].remove(city)
            self.route.append(city)
            valid = self.dfs(city, k)
            if valid:
                return valid
            self.route.pop()
            self.d[start].append(city)
 

    
solution = Solution()
#tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
print(solution.findItinerary(tickets))
