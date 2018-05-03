class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        index=[arr[i] for i in sorted(arr)]
        index=sorted(range(len(arr)), key=arr.__getitem__)
        print(index)
        maximum = 0
        temp = 0
        for i, x in enumerate(index):
            temp = max(temp, x)
            if temp == i: maximum += 1
        return maximum