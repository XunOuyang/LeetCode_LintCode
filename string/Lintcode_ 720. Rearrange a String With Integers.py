class Solution:
    """
    @param str: a string containing uppercase alphabets and integer digits
    @return: the alphabets in the order followed by the sum of digits
    """
    def rearrange(self, strs):
        # Write your code here
        temp = 0
        string = []
        flag = False
        for c in strs:
            if c.isdigit():
                flag = True
                temp += int(c)
            else:
                string.append(c)
        string.sort()
        if flag:
            return "".join(string) + str(temp)
        return "".join(string)
