# -*- coding: utf-8 -*-
"""
Created on Thu May 17 17:16:11 2018

@author: tzlmyq
"""
import collections

class TrieNode():
    def __init__(self):
        self.word = False
        self.children = collections.defaultdict(TrieNode)

        
class Trie(object):
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for c in word:
            node = node.children[c]
        node.word = True
        
    def search(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.word
    
    # understand the difference between search function and startswith function
    # search function will return only when it is a word, that is also why we need self.word = False to be initiated at the beginning
    # if it just needs us to find the prefix of it, then we need to 
    def startsWith(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True
   
