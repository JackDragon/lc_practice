class Solution:
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        one, two = set(), set()
        s_map = {}
        next_dislikes = []
        while True:
            if not dislikes:
                # print(list(one), list(two))
                return True
            for a, b in dislikes:
                if a in s_map and b in s_map:
                    if s_map[a] == s_map[b]:
                        return False
                    continue
                elif a in s_map:
                    s_map[b] = (s_map[a] + 1) %2
                    if s_map[b] == 0:
                        one.add(b)
                    else:
                        two.add(b)
                elif b in s_map:
                    s_map[a] = (s_map[b] + 1) %2
                    if s_map[a] == 0:
                        one.add(a)
                    else:
                        two.add(a)
                else:
                    next_dislikes.append([a,b])
            if len(dislikes) == len(next_dislikes):
                a,b = next_dislikes.pop()
                s_map[a] = 0
                one.add(a)
                s_map[b] = 1
                two.add(b)
            # print(dislikes, next_dislikes)
            dislikes, next_dislikes = next_dislikes, []
            # print(dislikes, next_dislikes)