# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        def height(root):
            # return 0, means the root is balanced
            if root is None: return 0
            
            # Post order traversal
            lefty = height(root.left)
            righty = height(root.right)
            
            # if the value is -1 or > 1, its not balanced
            if lefty == -1 or righty == -1 or abs(lefty - righty) > 1:
                return -1 
            
            # gives the height of each node
            return max(lefty, righty) + 1
        
        # returns the output if its balanced or not
        return height(root) != -1