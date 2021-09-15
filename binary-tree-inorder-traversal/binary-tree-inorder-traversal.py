# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        arr = []
        # start the recursion
        self.inorder(root, arr)
        return arr
    
    def inorder(self, root, arr):
        if root:
            # goes to the left-end of the root
            self.inorder(root.left, arr)
            # appends the val of root
            arr.append(root.val)
            # goes to the right-end of the root
            self.inorder(root.right, arr)
        