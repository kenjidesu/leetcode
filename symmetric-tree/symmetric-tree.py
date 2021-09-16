# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        def isSymm(l, r):  
            # checks nodes of left and right whether it is mirroring itself
            if l and r and l.val == r.val:
                return isSymm(l.left, r.right) and isSymm(l.right, r.left)
            
            return l == r
        
        # returns True if root is empty or passes r.l and r.r
        return not root or isSymm(root.left, root.right)