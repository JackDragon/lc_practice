class Solution(object):
    # def longestPalindrome(self, s):
    #     """
    #     :type s: str
    #     :rtype: str
    #     """
    #     length = len(s)
    #     par = [{} for _ in range(length)]
    #     def helper(i, j):
    #         # print("i,j: ", i, j)
    #         # print(str(par))
    #         if j in par[i]:
    #             return
    #         if (i == j):
    #             par[i][j] = 1
    #             return
    #         if (j-i == 1):
    #             par[i][j] = 2 if s[i] == s[j] else 0
    #         else:
    #             # print("i+1, j-1:", i+1, j-1)
    #             if j-1 not in par[i+1]:
    #                 helper(i+1, j-1)
    #             # else:
    #             #     print(j-1, "in", str(par[i+1]))
    #             par[i][j] = par[i+1][j-1] + 2 if s[i] == s[j] and par[i+1][j-1] else 0
    #     for i in range(length):
    #         for j in range(i, length):
    #             helper(i,j)
    #     longest, longest_i, longest_j = 1, 0, 0
    #     for i in range(length):
    #         for j in range(i, length):
    #             if par[i][j]>longest:
    #                 longest, longest_i, longest_j = j-i+1, i, j
    #     # print(str(par))
    #     return s[longest_i:longest_j+1]
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_len = len(s)
        l, h = 0, 0
        max_len, start, end = 1, 0, 0
        while l < s_len:
            l, h = getBoundary(s, l)
            ext_l, ext_h = extendPalindrome(s, l, h)
            if ext_h - ext_l + 1 > max_len:
                max_len = ext_h - ext_l + 1
                start = ext_l
                end = ext_h
            l = h + 1
        return s[start:end+1]

def getBoundary(s, start):
    """
    """
    end = start
    for i in range(start+1, len(s)):
        if s[i] != s[i-1]:
            end = i-1
            break;
        end = i
    return (start, end)

def extendPalindrome(s, start, end):
    """
    """
    offset = 0
    for off in range(0, min(start, len(s) - end - 1) + 1):
        if s[start-off] != s[end+off]:
            offset = off - 1
            break
        offset = off
    return (start - offset, end + offset)