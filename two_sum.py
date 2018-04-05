class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numss = sorted(nums)
        for i in range(len(numss)):
            current = numss[i]
            j = i+1
            while j < len(numss):
                if current + numss[j] == target:
                    return [nums.index(current), len(nums)-1-nums[::-1].index(numss[j])]
                elif current + numss[j] > target:
                    break
                else:
                    j += 1