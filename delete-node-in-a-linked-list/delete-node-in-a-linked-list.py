# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        # updates the val of the node to next node val
        node.val = node.next.val
        # connects to the next node of copied val
        node.next = node.next.next
            
        