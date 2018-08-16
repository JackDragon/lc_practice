# from collections import defaultdict
class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        c_d = set()
        bad = set()
        for word in A.split(" "):
            if word not in c_d:
                c_d.add(word)
            else:
                bad.add(word)
        c_d2 = set()
        for word in B.split(" "):
            if word not in c_d2:
                c_d2.add(word)
            else:
                bad.add(word)
        return list(c_d.symmetric_difference(c_d2).difference(bad))