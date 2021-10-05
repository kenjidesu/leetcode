# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """
    Explanation:
    https://www.youtube.com/watch?v=py3R23aAPCA
    """
    def lowestCommonAncestor(self, root, p, q):
        if root is None: return None
        
        if root.val == p.val or root.val == q.val:\
            return root
        
        lefty = self.lowestCommonAncestor(root.left, p, q)
        righty = self.lowestCommonAncestor(root.right, p, q)
        
        if lefty is None: return righty
        if righty is None: return lefty
        
        return root
        
        