# -*- coding: utf-8 -*-
"""
Created on Wed May 09 17:46:19 2018

@author: tzlmyq
"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = dict()
        res = []
        for string in strs:
            temp = "".join(sorted(string))
            if temp not in d.keys():
                d[temp] = [string]
            else:
                d[temp].append(string)
        for key in d.keys():
            sub_res = []
            for value in d[key]:
                sub_res.append(value)
            res.append(sub_res)
        return res
    
solution = Solution()
strs =  ["eat", "tea", "tan", "ate", "nat", "bat"]
print solution.groupAnagrams(strs)
