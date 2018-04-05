class Solution(object):
    def long(s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        longest = 1
        longest_s = ""
        a, b = 0, 0
        sub = ""
        while b < len(s):
            if s[b] in sub:
                print("Found {} in {}".format(s[b], sub))
                if len(sub) > longest:
                    longest = len(sub)
                    longest_s = sub
                a += sub.index(s[b]) + 1
                sub = s[a:b]
                print("Sub now: {}".format(sub))
            sub += s[b]
            b += 1
        if len(sub) > longest:
            longest = len(sub)
            longest_s = sub
        return longest, longest_s
    
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        longest = 1
        # longest_s = ""
        a, b = 0, 0
        sub = ""
        while b < len(s):
            if s[b] in sub:
                # print("Found {} in {}".format(s[b], sub))
                if len(sub) > longest:
                    longest = len(sub)
                    # longest_s = sub
                a += sub.index(s[b]) + 1
                sub = s[a:b]
                # print("Sub now: {}".format(sub))
            sub += s[b]
            b += 1
        if len(sub) > longest:
            longest = len(sub)
        return longest