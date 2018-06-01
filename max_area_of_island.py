class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited = set()
        stack = []
        max_size = 0
        MAX_I, MAX_J = (len(grid), len(grid[0]))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) in visited or not grid[i][j]:
                    continue
                size = 0
                stack = [(i, j)]
                while stack:
                    item = stack.pop()
                    if item in visited:
                        continue
                    # print(item)
                    for pair in [(item[0] - 1, item[1]), (item[0] + 1, item[1]), (item[0], item[1] - 1),
                                 (item[0], item[1] + 1)]:
                        if pair not in visited and MAX_I > pair[0] >= 0 and MAX_J > pair[1] >= 0 and grid[pair[0]][
                            pair[1]] == 1:
                            stack.append(pair)
                    visited.add(item)
                    size += 1
                max_size = max(max_size, size)
        return max_size
