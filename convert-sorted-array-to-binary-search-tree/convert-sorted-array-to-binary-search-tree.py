# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        return self.heib(nums, 0, len(nums))
    
    def heib(self, nums, lower, upper):
        # returns None at the very end of the node
        if lower == upper: return None
        
        # set the value of nums[mid] to the node
        mid = (lower + upper) // 2
        node = TreeNode(nums[mid])
        
        # continuously breaks the array into half (Binary Search)
        node.left = self.heib(nums, lower, mid)
        node.right = self.heib(nums, mid+1, upper)
        
        return node
        