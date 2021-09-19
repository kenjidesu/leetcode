# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        # Iterative Pre-order Traversal
        stck, vl = [root], []
        while stck:
            # pop() stck
            node = stck.pop()
            if node:
                # append to vl
                vl.append(node.val)
                stck.append(node.right)
                stck.append(node.left)
        
        return vl