class Solution:
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        total_len = 0
        overcount = 0
        word_set = set()
        words.sort(key=len,reverse=True)
        for word in words:
            if word in word_set:
                overcount += 1
            else:
                for i in range(len(word)):
                    word_set.add(word[i:])
                total_len += len(word)
        return total_len + len(words) - overcount