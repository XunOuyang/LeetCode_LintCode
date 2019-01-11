# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 21:56:04 2018

@author: TZLMYQ
"""
import collections
class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        dq = collections.deque()
        d = dict()
        res = 0
        temp = 0
        for i in range(len(tree)):
            if tree[i] not in d and len(d) < 2:
                dq.append(tree[i])
                d[tree[i]] = i
                temp += 1
            elif tree[i] not in d and len(d) == 2:
                t = dq.popleft()
                dq.append(tree[i])
                d[tree[i]] = i
                del d[t]
                temp = i + 1 - d[dq[0]]
            elif len(dq) == 2 and tree[i] == dq[0]:
                dq[0], dq[1] = dq[1], dq[0]
                d[dq[1]] = i
                temp += 1
            else:
                temp += 1
            print dq, d, temp
            res = max(temp, res)
        return res
            
solution = Solution()
tree = [0, 1, 2, 2]
print(solution.totalFruit(tree))