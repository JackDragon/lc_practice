class Solution:
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        bads = set()
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                bads.add(fronts[i])
        smallest = 9223372036854775807
        for i in range(len(fronts)):
            if fronts[i] not in bads:
                smallest = min(smallest, fronts[i])
            if backs[i] not in bads:
                smallest = min(smallest, backs[i])
        if smallest == 9223372036854775807:
            return 0
        return smallest