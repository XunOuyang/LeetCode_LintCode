# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 11:23:15 2018

@author: TZLMYQ
"""

"""
Making use of Trie to do word search
"""
import collections
class TrieNode(object):
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
            node = node.children.get(c)
        return node.word