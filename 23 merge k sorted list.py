# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 10:04:15 2018

@author: tzlmyq
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from operator import attrgetter

class Solution(object):
    def mergeKLists(self, lists):
        sorted_list = []
        for lis in lists:
            while lis:
                sorted_list.append(lis)
                if lis.next:
                    lis = lis.next
        sorted_list.sort(key=attrgetter(val), reverse=True)
        DummyNode = ListNode(0)
        root = DummyNode.next
        if sorted_list:
            while sorted_list:
                root = sorted_list.pop()
                root = root.next
            return DummyNode.next
        return None
    
    
        
                