# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.levels = {}
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.enqueue(root, 0)
        # return max(self.left, self.right)
        return max_no_adj(self.levels)
    def enqueue(self, node, level):
        self.levels[level] = node.val + self.levels[level] if level in self.levels else node.val
        if node.left:
            self.enqueue(node.left, level+1)
        if node.right:
            self.enqueue(node.right, level+1)
def max_no_adj(d):
    sum1 = 0
    sum2 = 0  
    for i in sorted(d.keys()):        
        # Current max excluding i
        temp = sum2 if sum2>sum1 else sum1
        sum1 = sum2 + d[i]
        sum2 = temp
    return max(sum2, sum1)