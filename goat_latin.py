class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowels = set(['a', 'e', 'i', 'o','u'])
        counter = 1
        S = S.split(" ")
        for i in range(len(S)):
            w = S[i]
            if w[0].lower() not in vowels:
                S[i] = w[1:] + w[0]
            S[i] += "ma" + counter*"a"
            counter += 1
        return " ".join(S, )