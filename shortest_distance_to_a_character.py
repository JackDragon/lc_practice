class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        cmap = set()
        l = []
        for i in range(len(S)):
            if S[i] == C:
                cmap.add(i)
        for i in range(len(S)):
            if S[i] == C:
                l.append(0)
            else:
                l.append(min([abs(i - n) for n in cmap]))
        return l
