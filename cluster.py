# -*- coding: utf-8 -*-
"""
Created on Fri May 18 17:10:36 2018

@author: tzlmyq
"""

import collections
class Solution(object):
    def clustering(self, graph):
        if graph == [] or graph == [[]]:
            return []
        res = []
        d = dict()
        tag = 1
        for pair in graph:
            # add new pair to the storage place
            # cannot revise the key directly
            if pair[0] not in d and pair[1] not in d:
                d[pair[0]] = tag
                d[pair[1]] = tag
                tag += 1
            # merge two sublist if the coming pair 
            elif pair[0] in d and pair[1] in d:
                tmp = max(d[pair[0]], d[pair[1]])
                d[pair[0]] = min(d[pair[0]], d[pair[1]])
                d[pair[1]] = min(d[pair[0]], d[pair[1]])
                org = d[pair[1]]
                for key, value in d.items():
                    if value == tmp:
                        d[key] = org        
            else:
                if pair[0] in d:
                    d[pair[1]] = d[pair[0]]
                else:
                    d[pair[0]] = d[pair[1]]
        cluster = collections.defaultdict(list)
        for key, val in d.items():
            cluster[val].append(key)
        for key in cluster:
            res.append(cluster[key])
        return res
                
solution = Solution()
graph = [[1,2], [3,4], [5,6], [2,3], [4,1]]
solution.clustering(graph)
