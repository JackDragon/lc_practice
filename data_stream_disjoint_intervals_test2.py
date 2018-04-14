# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class SummaryRanges(object):

    def __init__(self):
        self.intervals = []

    def addNum(self, val):
        heapq.heappush(self.intervals, (val, Interval(val, val)))

    def getIntervals(self):
        stack = []
        while self.intervals:
            idx, cur = heapq.heappop(self.intervals)
            if not stack:
                stack.append((idx, cur))
            else:
                _, prev = stack[-1]
                if prev.end + 1 >= cur.start:
                    prev.end = max(prev.end, cur.end)
                else:
                    stack.append((idx, cur))
        self.intervals = stack
        return list(map(lambda x: x[1], stack))


# Your SummaryRanges object will be instantiated and called as such:
obj = SummaryRanges()
# a = []
# for _ in range(100):
#    a.append(random.randint(0,100))
seq = [4, 1, 71, 0, 31, 37, 18, 29, 62, 38, 77, 54, 20, 53, 64, 47, 98, 50, 43, 34, 47, 68, 5, 56, 6, 84, 81, 47, 19, 64, 28, 16, 86, 51, 43, 29, 4, 38, 37, 78, 14, 86, 48, 50, 26, 93, 54, 17, 8, 43, 34, 30, 26, 95, 53, 100, 13, 89, 46, 47, 93, 69, 16, 95, 17, 83, 96, 57, 82, 99, 25, 86, 44, 100, 21, 32, 38, 60, 35, 90, 57, 23, 21, 99, 24, 76, 40, 66, 79, 85, 66, 39, 54, 77, 46, 27, 98, 19, 68, 82]
for i in seq:
    obj.addNum(val)
print(obj.getIntervals())
# param_2 = obj.getIntervals()