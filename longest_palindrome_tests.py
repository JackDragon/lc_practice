class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = 1
        longest_i = 0
        longest_j = 0
        length = len(s)
        par = [{}] * length
        def helper(i, j):
            if j in par[i]:
                return
            if (i == j):
                par[i][j] = 1
                return
            if (j-i == 1):
                par[i][j] = 1 if s[i] == s[j] else 0
            else:
                par[i][j] = par[i+1][j-1] + 2 if s[i] == s[j] and par[i+1][j-1] else 0
                if par[i][j] > longest:
                    longest_i, longest_j = i,j
        for i in range(length):
            for j in range(i, length):
                helper(i,j)
        return s[longest_i:longest_j+1]

def longestPalindrome(s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        par = [{} for _ in range(length)]
        def helper(i, j):
            # print("i,j: ", i, j)
            # print(str(par))
            if j in par[i]:
                return
            if (i == j):
                par[i][j] = 1
                return
            if (j-i == 1):
                par[i][j] = 2 if s[i] == s[j] else 0
            else:
                # print("i+1, j-1:", i+1, j-1)
                if j-1 not in par[i+1]:
                    helper(i+1, j-1)
                # else:
                #     print(j-1, "in", str(par[i+1]))
                par[i][j] = par[i+1][j-1] + 2 if s[i] == s[j] and par[i+1][j-1] else 0
        for i in range(length):
            for j in range(i, length):
                helper(i,j)
        longest, longest_i, longest_j = 1, 0, 0
        for i in range(length):
            for j in range(i, length):
                if par[i][j]>longest:
                    longest, longest_i, longest_j = j-i+1, i, j
        # print(str(par))
        return s[longest_i:longest_j+1]

longestPalindrome("babad")

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = 1
        longest_i = 0
        longest_j = 0
        length = len(s)
        par = [{}] * length
        def helper(i, j):
            if j in par[i]:
                return
            if (i == j):
                par[i][j] = 1
                return
            if (j-i == 1):
                par[i][j] = 1 if s[i] == s[j] else 0
            else:
                par[i][j] = par[i+1][j-1] + 2 if s[i] == s[j] and par[i+1][j-1] else 0
                if par[i][j] > longest:
                    longest_i, longest_j = i,j
        for i in range(length):
            for j in range(i, length):
                helper(i,j)
        return s[longest_i:longest_j+1]

def longestPalindrome(s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        par = [{} for _ in range(length)]
        def helper(i, j, longest, longest_i, longest_j):
            # print(longest, longest_i, longest_j)
            # print("i,j: ", i, j)
            # print(str(par))
            if j in par[i]:
                return longest, longest_i, longest_j
            if (i == j):
                par[i][j] = 1
                return longest, longest_i, longest_j
            if (j-i == 1):
                par[i][j] = 1 if s[i] == s[j] else 0
            else:
                # print("i+1, j-1:", i+1, j-1)
                if j-1 not in par[i+1]:
                    helper(i+1, j-1)
                # else:
                #     print(j-1, "in", str(par[i+1]))
                par[i][j] = par[i+1][j-1] + 2 if s[i] == s[j] and par[i+1][j-1] else 0
                if par[i][j] > longest:
                    return par[i][j],i,j
                return longest, longest_i, longest_j
        for i in range(length):
            for j in range(i, length):
                longest, longest_i, longest_j = helper(i,j,longest,longest_i,longest_j)
        # print(str(par))
        print(longest, longest_i, longest_j)
        return s[longest_i:longest_j+1]

longestPalindrome("babad")