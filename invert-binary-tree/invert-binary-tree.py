# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        if root:
            lefts = self.invertTree(root.left)
            rights = self.invertTree(root.right)
            
            root.right = lefts
            root.left = rights
        
        return root