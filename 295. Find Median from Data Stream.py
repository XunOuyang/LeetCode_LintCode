# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 19:32:29 2018

@author: tzlmyq
"""

from queue import PriorityQueue
class MedianFinder(object):
    """
    Before starting to solve this problem, we have to understand what is the concept of median number -- If the size of the list is even, median is the mean of the two middle value, i.e., the mean of the minimum of the bigger half and the maximum of the smaller half
    """
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxHeap = PriorityQueue()
        self.minHeap = PriorityQueue()

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        self.maxHeap.put(-num)
        self.minHeap.put(-self.maxHeap.get())
        if self.minHeap.qsize() > self.maxHeap.qsize():
            self.maxHeap.put(-self.minHeap.get())
        
        
    def findMedian(self):
        """
        :rtype: float
        """
        if self.maxHeap.qsize() > self.maxHeap.qsize():
            temp = -self.maxHeap.get()
            self.maxHeap.put(-temp)
            return temp
        else:
            maxH = -self.maxHeap.get()
            self.maxHeap.put(maxH)
            minH = self.minHeap.get()
            self.minHeap.put(minH)
            return (minH - maxH)/2.0
        
m = MedianFinder()
m.addNum(1)
print(m.findMedian())
m.addNum(2)
print(m.findMedian())
m.addNum(3)
print(m.findMedian())