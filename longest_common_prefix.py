import re
class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        d = {}
        for s in paragraph.lower().split(" "):
            s = re.sub('[^A-Za-z0-9]+', '', s)
            if s not in banned:
                if s in d:
                    d[s]+=1
                else:
                    d[s]=1
        mx = max(d.values())
        # print(d)
        for k, v in d.items():
            if v == mx:
                return(k)