# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        if root is None: return 0
        
        # Post Order Traversal
        x = self.minDepth(root.left)
        y = self.minDepth(root.right)
        
        # if skewedTree it'll return the max(x, y)
        # else will return the min(x, y)
        return 1 + max(x, y) if x == 0 or y == 0 else 1 + min(x, y)
        