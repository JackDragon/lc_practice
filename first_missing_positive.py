class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            # print(nums)
            nums = helper(i, nums)
        # print(nums)
        for i in range(len(nums)):
            if not nums[i]:
                return i+1
        return len(nums)+1  

def helper(i, a):
    # print("helper", i, a)
    j = a[i]
    if j == i+1 or j == 0:
        return a
    if j < 1 or j > len(a):
        a[i] = 0
    # elif j == i:
    #     a[j] = 0
    #     a = helper(i, a)
    else:
        a[j-1], a[i] = j if j > 0 else 0, a[j-1] if a[j-1] > 0 and a[j-1] != a[i] else 0
        a = helper(i, a)
    return a


print("Should be: 4, 2, 1, 1, 5, 3, 2")
print(firstMissingPositive([1, 0, -1, 2, 3, 5]))
print(firstMissingPositive([1]))
print(firstMissingPositive([-1]))
print(firstMissingPositive([-1, 0]))
print(firstMissingPositive([-1, 0, 1, 3, 2, 4, 7]))
print(firstMissingPositive([2, 1]))
print(firstMissingPositive([3,4,-1,1]))
