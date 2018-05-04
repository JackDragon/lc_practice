class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        ind=sorted(range(len(arr)), key=arr.__getitem__)
        max_n = temp = 0
        for i, x in enumerate(ind):
            temp = max(temp, x)
            if temp == i: max_n += 1
        return max_n