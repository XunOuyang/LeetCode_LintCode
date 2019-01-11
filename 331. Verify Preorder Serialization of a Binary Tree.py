# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 21:26:33 2018

@author: tzlmyq
"""

class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        if not preorder:
            return True
        if preorder[0] == "#" and len(preorder) > 1:
            return False
        preorder = preorder.split(",")
        counter = 1
        for char in preorder:            
            counter -= 1
            # be careful that we need to put the counter condition here
            if counter < 0:
                return False
            if char != "#":
                counter += 2
            
        return counter == 0
    
    
preorder = "1,#"