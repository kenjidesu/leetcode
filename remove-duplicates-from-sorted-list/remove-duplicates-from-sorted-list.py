# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        if head is None:
            return head
        
        cur, pred, = head, head.next
        while cur.next:
            if cur.val == pred.val:
                cur.next = pred.next
                pred = cur.next
            else:
                cur = pred
                pred = pred.next
                
        return head
        