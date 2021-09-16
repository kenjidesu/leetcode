"""
What is p is q?
It is just to return True if p == None and q == None else False.

It recursively checks each node of p and q and compare it to each other and if one of the
node are not equal to the other node it'll return False.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        # recursively check if p's and q's node are equal
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # returns if p and q are the same object
        return p is q
        
