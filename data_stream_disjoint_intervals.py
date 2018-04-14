# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        if val in self.dic:
            return
        else:
            self.dic[val] = 1
        if val + 1 in self.dic:
            self.dic[val], self.dic[val + 1] = self.dic[val] + self.dic[val + 1], 0
        previous = val - 1
        if previous not in self.dic or previous <= 0:
            return
        while True:
            if self.dic[previous] == 0 and previous - 1 in self.dic:
                previous -= 1
            else:
                break
        self.dic[previous], self.dic[val] = self.dic[previous] + self.dic[val], 0

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        return [Interval(x, x + self.dic[x] - 1) for x in sorted(self.dic) if self.dic[x] > 0]


# Your SummaryRanges object will be instantiated and called as such:
obj = SummaryRanges()
# a = []
# for _ in range(100):
#    a.append(random.randint(0,100))
seq = [4, 1, 71, 0, 31, 37, 18, 29, 62, 38, 77, 54, 20, 53, 64, 47, 98, 50, 43, 34, 47, 68, 5, 56, 6, 84, 81, 47, 19, 64, 28, 16, 86, 51, 43, 29, 4, 38, 37, 78, 14, 86, 48, 50, 26, 93, 54, 17, 8, 43, 34, 30, 26, 95, 53, 100, 13, 89, 46, 47, 93, 69, 16, 95, 17, 83, 96, 57, 82, 99, 25, 86, 44, 100, 21, 32, 38, 60, 35, 90, 57, 23, 21, 99, 24, 76, 40, 66, 79, 85, 66, 39, 54, 77, 46, 27, 98, 19, 68, 82]
for i in seq:
    obj.addNum(i)
print([(iv.start, iv.end) for iv in obj.getIntervals()])
# param_2 = obj.getIntervals()