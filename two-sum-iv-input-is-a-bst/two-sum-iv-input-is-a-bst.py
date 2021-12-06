# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        # track the complements
        hsm = set()
        
        def findK(root):
            if root:
                complement = k - root.val
                # checks if the complement is in hsm
                if complement in hsm:
                    return True
                # Add root.val
                hsm.add(root.val)
                
                # return True, if one of the tree is returned True otherwise False
                return findK(root.left) or findK(root.right)
        
        return findK(root)
        