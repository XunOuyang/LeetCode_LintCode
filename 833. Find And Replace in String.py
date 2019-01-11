# -*- coding: utf-8 -*-
"""
Created on Sat May 12 22:17:09 2018

@author: tzlmyq
"""

def findReplaceString( S, indexes, sources, targets):
    """
    :type S: str
    :type indexes: List[int]
    :type sources: List[str]
    :type targets: List[str]
    :rtype: str
    """
    if not S:
        return S
    s = list(S)
    combo = []
    for i in range(len(indexes)):
        combo.append([indexes[i], sources[i], targets[i]])
    combo.sort()
    for i in range(len(sources)):
        if S.find(combo[i][1]) == combo[i][0]:
            if len(combo[i][1]) == len(combo[i][2]):
                s[combo[i][0]:combo[i][0]+ len(combo[i][1])] = combo[i][2]
            else:
                print i,s, combo[i][0], combo[i][2], len(s)
                s[combo[i][0]] = combo[i][2]
                for j in range(i + 1, i + len(combo[i][1] )-1):
                        s[j] = ""
    return "".join(s)
    

S = "abcd"
indexes =[0, 2]
sources = ["a", "cd"]
targets = ["eee", "ffff"]


'''
S = "frheltogokypgwyoafpp"
indexes =[15,10,8,5,17,2]
sources = ["oa","yp","ok","tog","fp","hel"]
targets = ["fth","ml","vky","fw","k","yzat"]
'''

print findReplaceString( S, indexes, sources, targets)