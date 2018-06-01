class Solution:
    def __init__(self):
        self.memo = {}
    def splitIntoFibonacci(self, S):
        x = self.s_helper(S)
        if not x:
            return x
        return [int(i) for i in x]
    def s_helper(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        if S in self.memo:
            return self.memo[S]
        if len(S) < 3:
            self.memo[S] = []
            return []
        if len(S) == 3 and isFib(S[0], S[1], S[2]):
            self.memo[S] = [S[0], S[1], S[2]]
            return [S[0], S[1], S[2]]
        for i in range(1, len(S) + 1):
            for j in range(i+1, len(S)+1):
                # print(S[:i], S[i:j], S[j:])
                if isFib(S[:i], S[i:j], S[j:]):
                    self.memo[S] = [S[:i], S[i:j], S[j:]]
                    return [S[:i], S[i:j], S[j:]]
        for i in range(1, len(S) + 1):
            # print(S[:i])
            if S[0] == "0" and i>1:
                continue
            sp = self.s_helper(S[i:])
            if not sp:
                continue
            if isFib(S[:i], sp[0], sp[1]):
                self.memo[S] = [S[:i]] + sp
                return [S[:i]] + sp
        self.memo[S] = []
        return []

    # def splitIntoFibonacciHelper(self, S):
    #     if len(S) < 3:
    #         return False
    #     if len(S) == 3 and isFib(S[0], S[1], S[2]):
    #         return [S[0], S[1], S[2]]
    #     for i in range(1, len(S) + 1):
    #         sp = s_helper(S[i:])
    #         if not sp:
    #             continue
    #         if isFib(S[:i], sp):
    #             return ([S[:i]] + sp)
    #     if isFib(S[0], s_helper(S[1:]))

def isFib(i, j, k):
    for n in [i,j,k]:
        if not n or (n.startswith('0') and len(n) > 1):
            return False
    # print(i, j, k, (int(i) + int(j)) == int(k))
    return (int(i) + int(j)) == int(k)

solution = Solution()
print(solution.s_helper("123456579"))
print(solution.s_helper("214748364721474836422147483641"))
print(solution.s_helper("539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511"))