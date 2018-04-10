class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        l, n = len(s), 0
        for i in range(l):
            j = s[i]
            # A = 65
            n += (ord(j)-64) * 26 ** (l-i-1)
        return n