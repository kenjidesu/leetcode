# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        hsm = set()
        
        def findK(root):
            if root:
                deduc = k - root.val
                if deduc in hsm:
                    return True
                hsm.add(root.val)

                return findK(root.left) or findK(root.right)
        
        return findK(root)
        
        