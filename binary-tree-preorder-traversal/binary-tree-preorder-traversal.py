# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        arr = []
        def binTree(root):
            if root:
                arr.append(root.val)
                binTree(root.left)
                binTree(root.right)
        
        binTree(root)
        return arr
        