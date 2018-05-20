class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        # return ((rec2[0] < rec1[0] < rec2[2] and rec2[1] < rec1[1] < rec2[3])
        #     or (rec1[0] < rec2[0] < rec1[2] and rec1[1] < rec2[1] < rec1[3])
        #     or (rec2[0] < rec1[2] < rec2[2] and rec2[1] < rec1[3] < rec2[3])
        #     or (rec1[0] < rec2[2] < rec1[2] and rec1[1] < rec2[3] < rec1[3]))
        if (rec1[0] >= rec2[2]) or (rec1[2] <= rec2[0]):
            return False
        if (rec1[3] <= rec2[1]) or (rec1[1] >= rec2[3]):
            return False
        return True