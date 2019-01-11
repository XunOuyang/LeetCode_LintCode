# -*- coding: utf-8 -*-
"""
Created on Sun May 27 23:10:42 2018

@author: tzlmyq
"""
import collections
import random
class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.index = 0
        self.data = []
        self.position = collections.defaultdict(set)
        
    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """        
        self.position[val].add(self.index)
        self.data.append(val)
        self.index += 1
        return len(self.position[val]) == 1

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if self.position[val]:
            
            out = self.position[val].pop()
            ins = self.data[-1]
            self.data[out] = self.data[-1]
            if self.position[self.data[-1]]:                
                self.position[self.data[-1]].add(out)
                self.position[self.data[-1]].discard(len(self.data) - 1)
            self.data.pop()            
            self.index -= 1
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return random.choice(self.data)
    
a = RandomizedCollection()
a.insert(4)
a.insert(3)
a.insert(4)
a.insert(2)
a.insert(4)
print a.position, a.data
a.remove(4)
print a.position, a.data
a.remove(3)
print a.position, a.data
a.remove(4)
a.remove(4)
["RandomizedCollection","insert","insert","insert","insert","insert","remove","remove","remove","remove"]
[[],[4],[3],[4],[2],[4],[4],[3],[4],[4]]