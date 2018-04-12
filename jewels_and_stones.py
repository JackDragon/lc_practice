class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        # total = 0
        # # d = {x:[] for x in J}
        # for y in S:
        #     # if y in d:
        #     if y in J:
        #         total += 1
        # return total
        J = set(J)
        return sum(s in J for s in S)