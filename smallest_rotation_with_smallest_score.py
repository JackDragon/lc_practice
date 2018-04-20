# Example 1:
# Input: [2, 3, 1, 4, 0]
# Output: 3
# Explanation:  
# Scores for each K are listed below: 
# K = 0,  A = [2,3,1,4,0],    score 2
# K = 1,  A = [3,1,4,0,2],    score 3
# K = 2,  A = [1,4,0,2,3],    score 3
# K = 3,  A = [4,0,2,3,1],    score 4
# K = 4,  A = [0,2,3,1,4],    score 3
class Solution(object):
    def bestRotation(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        