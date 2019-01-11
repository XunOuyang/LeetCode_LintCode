# -*- coding: utf-8 -*-
"""
Created on Fri May 18 11:15:22 2018

@author: tzlmyq
"""

import collections

class TrieNode():
    def __init__(self):
        self.word = False
        self.children = collections.defaultdict()

class Trie():
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for c in word:
            node = node.children.get(c)
        node.word = True
        
    def search(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children.get(c)
        return node.word

class Solution(object):
    def findWords(self, board, words):
        trie = Trie()
        res = []
        node = trie.root
        for word in words:
            trie.insert(word)
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                self.dfs(board, node, i, j, "", res)
        return res
    
    def dfs(self, board, node, i, j, path, res):
        if node.word:
            res.append(path)
            node.word = False
        if i < 0 or i >= len(board) or j < 0 or j <= len(board[0]):
            return
        tmp = board[i][j]
        node = node.children.get(tmp)
        if not node:
            return
        board[i][j] = "#"
        self.dfs(board, node, i + 1, j, path + tmp, res)
        self.dfs(board, node, i - 1, j, path + tmp, res)
        self.dfs(board, node, i, j + 1, path + tmp, res)
        self.dfs(board, node, i, j - 1, path + tmp, res)
        board = tmp