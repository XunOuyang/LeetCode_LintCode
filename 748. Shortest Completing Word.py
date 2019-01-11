# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 23:27:02 2018

@author: tzlmyq
"""
import collections
class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        string = ""
        for char in licensePlate:
            if char.isalpha():
                string += char.lower()
        counter = collections.Counter(string)
        res = "asdfasdfasdfasdfasdfasdfasdf"
        for word in words:
            temp_counter = collections.Counter(word)
            flag = True
            for item in counter:
                if temp_counter[item] < counter[item]:
                    flag = False
                    break
            if flag and len(word) < len(res):
                res = word
        return res
    
    
solution = Solution()
licensePlate = "1s3 456"
words = ["looks","pest","stew","show"]
print solution.shortestCompletingWord(licensePlate, words)