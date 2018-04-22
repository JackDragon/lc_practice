class Solution:
    def numFactoredBinaryTrees(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        total = len(A)
        A.sort()
        visited = set([A[0]])
        # pairs = set()
        n_map = {}
        for n in A[1:]:
            for i in visited:
                for j in visited:
                    # if i >= j:
                    # # if i >= j and i*j == n:
                    #     total += 1
                    if i >= j and i * j == n:
                        if n not in n_map:
                            n_map[n] = 0
                        perms = 1
                        # if i == j:
                        #     n_map[n] += 1
                        # else:
                        #     n_map[n] += 2
                        if i != j:
                            perms = 2
                        # print(1, perms)
                        if i in n_map:
                            perms *= n_map[i] +1
                        if j in n_map:
                            perms *= n_map[j] +1
                        # print(2, perms)
                        n_map[n] += perms
                        # print(n_map)
                        # pairs.add((n, i, j))
                        # pairs.add((n, j, i))
                        total += perms
                    # print((n, i, j), total)
            visited.add(n)
        return total%(10**9+7)

# sol = Solution()
# sol.numFactoredBinaryTrees([2,4,5,10])
# sol.numFactoredBinaryTrees([18,3,6,2])