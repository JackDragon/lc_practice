class Solution:
    def numFactoredBinaryTrees(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        total = len(A)
        A.sort()
        visited = A
        visited.sort()
        # pairs = set()
        n_map = {}
        for n in A[1:]:
            for a in range(len(visited)):
                for b in range(a, len(visited)):
                    i, j = visited[a], visited[b]
                    # if i >= j:
                    # # if i >= j and i*j == n:
                    #     total += 1
                    if i >= n or j >= n:
                        continue
                    if j >= i and i * j == n:
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
                        # pairs.append((n, i, j))
                        # pairs.append((n, j, i))
                        total += perms
                    # print((n, i, j), total)
        return total%(10**9+7)