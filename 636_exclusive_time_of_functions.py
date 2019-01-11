# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 10:46:51 2018

@author: tzlmyq
"""

class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        log_files = []
        pool = set()
        while logs:
            log = logs.pop()
            log_files.append(log.split(":")+[0])
            pool.add(log.split(":")[0])
        res = [0] * len(pool)
        stack = []
        while log_files:            
            log = log_files.pop()
            if log[1] == "start":
                stack.append(log)
            else:
                print int(stack[-1][0])
                res[int(stack[-1][0])] += int(log[2]) - int(stack[-1][2]) + 1 - stack[-1][3]
                temp = int(log[2]) - int(stack[-1][2]) + 1 - stack[-1][3]
                stack.pop()
                if stack:
                    stack[-1][3] += temp
        return res
                    
                    
            
        """    
        for i in range(1, len(stack)):
            if stack[i-1][1] == "start" and stack[i][1] == "start":
                    res[int(stack[i-1][0])] += int(stack[i][2]) - int(stack[i-1][2])      
            elif stack[i-1][1] == "start" and stack[i][1] == "end":
                    res[int(stack[i][0])] += int(stack[i][2]) - int(stack[i-1][2]) + 1
            elif stack[i-1][1] == "end" and stack[i][1] == "end":
                    res[int(stack[i][0])] += int(stack[i][2]) - int(stack[i-1][2])
        return res
        """
        
        
solution = Solution()
n = 2
#logs = ["0:start:0","0:start:2","0:end:5","1:start:7","1:end:7","0:end:8"]
logs = ["0:start:0",
 "1:start:2",
 "1:end:5",
 "0:end:6"]

print solution.exclusiveTime(n, logs)
                