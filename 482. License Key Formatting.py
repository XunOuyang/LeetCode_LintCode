class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        s = ("".join(S.upper().split("-")))[::-1]
        res = ""
        i = 0
        while i < len(s)/K:
            res = res + s[K*i:K*(i+1)] + "-"
            i += 1
        if len(s)%K:
            res += s[K*i:K*(i+1)]
        else:
            res = res[:-1]
        return res[::-1]
