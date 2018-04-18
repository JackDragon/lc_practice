class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        i = 0
        ret_pre = ""
        while True:
            pre = ""
            for s in strs:
                if len(s) < i+1:
                    return ret_pre
                if not pre:
                    pre = s[i]
                elif pre != s[i]:
                    return ret_pre
            i += 1
            ret_pre += pre