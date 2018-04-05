class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(x)
        if "-" in s:
            i = int(s[:0:-1])
            return -i if i < 2147483647 else 0
        else:
            i = int(s[::-1])
            return i if i <= 2147483647 else 0