# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

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
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()