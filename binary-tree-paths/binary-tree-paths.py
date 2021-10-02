# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        arr = []
        # error check, if root exists
        if root is None:
            return arr
        
        self.recurTree(root, "", arr)
        return arr
    
    def recurTree(self, node, sti, arr):
        sti += str(node.val)
        # if there's no more children, append to arr
        if node.left is None and node.right is None:
            arr.append(sti)
            return
        
        # Traverse to all children of root and appending to sti
        if node.left is not None:
            self.recurTree(node.left, sti + "->", arr)
            
        if node.right is not None:
            self.recurTree(node.right, sti + "->", arr)
            
        
