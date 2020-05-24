class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <3:
            return True
        if s == s[::-1]:
            return True
        else:
            i,j = 0,len(s)-1            
            while i<j:
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                else:
                    return s[i:j] == s[-i-2:-j-2:-1] or s[i+1:j+1]==s[-i-1:-j-1:-1]
