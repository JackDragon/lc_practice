# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

# Example:

# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

# Note:

# Although the above answer is in lexicographical order, your answer could be in any order you want.

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        d = {'2':set(['a','b','c']),
             '3':set(['d','e','f']),
             '4':set(['g','h','i']),
             '5':set(['j','k','l']),
             '6':set(['m','n','o']),
             '7':set(['p','q','r','s']),
             '8':set(['t','u','v']),
             '9':set(['w','x','y','z']),
            }
        s = set()
        for digit in digits:
            if not s:
                s = d[digit].copy()
            else:
                temp = set()
                for old_str in s:
                    for new_str in d[digit]:
                        temp.add(old_str+new_str)
                s = temp
        return list(s)