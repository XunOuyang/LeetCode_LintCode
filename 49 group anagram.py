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
        '''
        count = 0
        dic = {}
        res = []
        for string in strs:
            if "".join(sorted(string)) in dic:
                res[dic["".join(sorted(string))]].append(string)
            else:
                dic["".join(sorted(string))] = count
                res.append([string])
                count += 1
        return res
        '''
    
        d = dict()
        res = []
        for string in strs:
            temp = "".join(sorted(string))
    #        print temp
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