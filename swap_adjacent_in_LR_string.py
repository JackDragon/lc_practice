class Solution(object):
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        # if not start and not end:
        #     return True
        if len(start) != len(end) or start.replace("X", "") != end.replace("X", ""):
            return False
        start_d, end_d = {"L":[], "R":[]}, {"L":[], "R":[]}
        for i, letter in enumerate(start):
            if letter == "X":
                continue
            start_d[letter].append(i)
        for i, letter in enumerate(end):
            if letter == "X":
                continue
            end_d[letter].append(i)
        # print(str(start_d), str(end_d))
        for i in range(len(start_d["L"])):
            if start_d["L"][i] < end_d["L"][i]:
                #print("L:" + str(start_d["L"][i]) + "<" + str(end_d["L"][i]))
                return False
        for i in range(len(start_d["R"])):
            if start_d["R"][i] > end_d["R"][i]:
                #print("R:" + str(start_d["R"][i]) + ">" + str(end_d["R"][i]))
                return False
        return True