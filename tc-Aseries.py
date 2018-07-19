from collections import defaultdict
class ASeries:
    def __init__(self):
        pass
    def longest(self, values):
        if not values:
            return 0
        val_map = defaultdict(int)
        for val in values:
            val_map[val] += 1
        if len(val_map.keys()) < 2:
            return max(max(val_map.values()), len(val_map.keys()))
        values = sorted(val_map.keys())
        prev = values[1]
        diff = values[1]-values[0]
        max_len = 2
        cur_len = 2
        for next in values[2:]:
            next_diff = next - prev
            if next_diff == diff:
                cur_len += 1
            else:
                cur_len = 2
                diff = next_diff
            if cur_len > max_len:
                max_len = cur_len
            prev = next
        return max(max(val_map.values()),max_len)

sol = ASeries()
print(sol.longest([3, 8, 4, 5, 6, 2, 2]))
print(sol.longest([-1, -5, 1, 3]))
print(sol.longest([-10, -20, -10, -10]))