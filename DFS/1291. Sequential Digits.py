"""
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

 

Example 1:

Input: low = 100, high = 300
Output: [123,234]
Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]

Follow up:
if it does not need to be sequentially increased,  how many numbers will be qualified?

Example 1:
Input: low = 100, high = 300
Output: 
Explanation: 123, 124... 129, 
             134, 13.... 139,
"""

class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        string = "123456789"
        res = []
        for i in range(len(str(low)), len(str(high))+1):
            for j in range(0, len(string)-i+1):
                if low <= int(string[j:j+i]) <= high:
                    res.append(int(string[j:i+j]))
        return res
                    
