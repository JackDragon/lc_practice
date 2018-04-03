## https://leetcode.com/problems/group-anagrams/description/
class Solution(object):
    
    def getIndex(s):
        d = {}
        for letter in s:
            if letter in d:
                d[letter] += 1
            else:
                d[letter] = 1
        ordered_keys = d.keys()
        ordered_keys.sort()
        return "".join(letter+str(d[letter]) for letter in ordered_keys)
    
    def groupReverse(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ret_list = []
        index = {}
        for s in strs:
            if s in index:
                ret_list[index[s]].append(s)
            else:
                index[s], index[s[::-1]] = len(ret_list), len(ret_list)
                ret_list.append([s])
        return ret_list
    
    def groupAnagrams(self, strs):
        def getIndex(s):
            d = {}
            for letter in s:
                if letter in d:
                    d[letter] += 1
                else:
                    d[letter] = 1
            ordered_keys = d.keys()
            ordered_keys.sort()
            return "".join(letter+str(d[letter]) for letter in ordered_keys)
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        index_dict = {}
        for s in strs:
            index = getIndex(s)
            if index in index_dict:
                index_dict[index].append(s)
            else:
                index_dict[index] = [s]
        return index_dict.values()