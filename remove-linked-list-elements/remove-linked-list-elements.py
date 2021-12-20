# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        if not head:
            return
        
        cur = head.next
        prev = head
        while cur:
            if cur.val == val:
                cur = cur.next
                prev.next = cur
            else:
                prev = cur
                cur = cur.next
            
        if head.val == val:
            return head.next
        
        return head
        