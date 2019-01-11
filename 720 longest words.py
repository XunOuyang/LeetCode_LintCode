# -*- coding: utf-8 -*-
"""
Created on Wed Aug 08 19:25:55 2018

@author: TZLMYQ
"""


class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        max_len = 0
        words.sort(key = lambda x:(len(x), x))
        for word in words:
            max_len = max(max_len, len(word))
        
        bucket = [[] for _ in range(max_len) ]
        for word in words:
            bucket[len(word)-1].append(word)
        stack = set(bucket[0])
        res = ""
        for i in range(1, len(bucket)):
            for word in bucket[i]:
                if word[:-1] in stack:
                    stack.add(word)
                    if len(word) > len(res):
                        res = word
        return res
    
    
solution = Solution()
words = ["a","banana","app","appl","ap","apply","apple"]
print solution.longestWord(words)

"""
import collections

class TrieNode(object):
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isEnd = False
        
class Trie(object):
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for c in word:
            node = node.children(c)
        node.isEnd = True
        
    def search(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children.get(c)
        return node.word
        



class Solution(object):
    def longestWord(self, words):
"""
        
 #       :type words: List[str]
 #       :rtype: str
    
"""
        trie = Trie()
        for word in words:
            trie.insert(word)
"""