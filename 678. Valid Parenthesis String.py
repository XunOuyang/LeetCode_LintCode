# -*- coding: utf-8 -*-
"""
惊讶的发现以前checkin到github里面的答案是错误的。
这道题用下面的方法很容易理解，但是最容易犯错的是，直接会忽略掉第28行到33行的代码，而这恰恰是关键。
"""

class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, star = [], []
        for i, c in enumerate(s):
            if c == "(":
                left.append(i)
            elif c == "*":
                star.append(i)
            else:
                if left:
                    left.pop()
                elif star:
                    star.pop()
                else:
                    return False
        if len(left) > len(star):
            return False
        while left:
            if left[-1] > star[-1]:
                return False
            else:
                left.pop()
                star.pop()
        return True
    
class Solution2:
    def checkValidString(self, s: str) -> bool:
        count = 0
        for c in s:
            if c == ")":
                count -= 1
                if count < 0:
                    return False
            else:
                count += 1
        if count == 0:
            return True
        count = 0
        for c in s[::-1]:
            if c == "(":
                count -= 1
                if count < 0:
                    return False
            else:
                count += 1
        return True
        
