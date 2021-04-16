# -*- coding: utf-8 -*-
"""
Created on Fri Aug 03 09:10:29 2018

@author: tzlmyq
"""

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False for _ in range(len(s))]
        for i in range(len(s)):
            for word in wordDict:
                if word == s[i:i + len(word)] and (i == 0 or dp[i - 1] == True):
                    dp[i + len(word) - 1] = True
        return dp[-1]
            
            
        
        
def test_wordBreak():
    solution = Solution()
    
    strings = ["catsandog", "leetcode"]
    wordDicts = [["dog",  "and", "cats"], ["leet", "code"]]
    answers = [False, True]
    for i in range(len(strings)):
        assert solution.wordBreak(strings[i], wordDicts[i]) == answers[i], "Failed at Test case " + str(i + 1)

if __name__ == "__main__":
    test_wordBreak()
    print("Pass")