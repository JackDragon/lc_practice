# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def __init__(self):
    #     self.levels = {}
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            d = {}
            return self.helper(root,d)
        return 0
    
    def helper(self,root, d):
        if not root:
            return 0        
        elif root in d:
            return d[root]
        else:
            a = self.helper(root.left.left,d) + self.helper(root.left.right,d) if root.left else 0
            b = self.helper(root.right.left,d) + self.helper(root.right.right,d) if root.right else 0
            
            maximum = max(root.val+a+b,self.helper(root.left,d)+self.helper(root.right,d))
            d[root] = d.get(root,0)  + maximum
            return maximum