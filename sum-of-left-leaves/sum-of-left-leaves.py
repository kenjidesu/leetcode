# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        def lefty(root, check):
            # checks if root is a root.left
            if check and root.left is None and root.right is None :
                self.ss += root.val
            
            # recurs with flag to know its a root.left
            if root.left:
                lefty(root.left, True)
            # False for root.right since we dont right's value
            if root.right:
                lefty(root.right, False)
            
            # return sum of left leaves
            return self.ss
        
        # checks if root exist
        if root is None:
            return 0
        # return value
        self.ss = 0
        # set check to False since its a parent node
        return lefty(root, False)