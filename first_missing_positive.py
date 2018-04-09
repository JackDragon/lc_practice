class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
def helper(i, nums):
    j = nums[i]
    if j < 0:
        nums[i] = 0
    else:
        nums = helper(j, nums)
        nums[j] = j
    return nums