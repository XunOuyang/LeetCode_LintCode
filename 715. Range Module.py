# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 18:51:59 2018

@author: TZLMYQ
"""
import bisect
class RangeModule(object):

    def __init__(self):
        self.module = []
        self.left = []
        self.right = []

    def addRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: void
        """
        if self.module == []:
            self.module = [[left, right]]
        else:
            i = bisect.bisect_left(self.left, left)
            j = bisect.bisect(self.right, right)
            if i > 0 and left <= self.module[i-1][1]:
                left = self.module[i-1][0]
                i -= 1
            if j < len(self.module)-1 and right >= self.module[j][0]:
                right = self.module[j][1]
                j += 1
            self.module[i:j] = [left, right]
        self.left = [item[0] for item in self.module]
        self.right = [item[1] for item in self.module]

    def queryRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: bool
        """
        i = bisect.bisect(self.left, left)
        j = bisect.bisect_left(self.right, right)
        return i == j

    def removeRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: void
        """
        i = bisect.bisect_left(self.left, left)
        j = bisect.bisect_left(self.right, right)
        print i, j
        if i < len(self.module) and self.left[i] == left and self.right[j] == right:
            del self.module[i:j+1]
        elif self.left[i] <= left and self.right[j] >= right:
            self.module[i:j+1] = [[self.module[i][0], left], [right, self.module[i][1]]]
        self.left = [item[0] for item in self.module]
        self.right = [item[1] for item in self.module]
            
solution = RangeModule()
solution.addRange(10,20)
print(solution.module)
solution.removeRange(14 ,16)
print(solution.module)
