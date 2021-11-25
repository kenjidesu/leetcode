# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        if head is None:
            return
        
        # return head if there's only 1 node
        if head.next is None:
            return head
        
        curr = head         # slow head
        pred = head.next    # fast head
        
        while curr.next:
            # if slow == fast, updates the next node of curr,
            # to get rid of the duplicate
            if curr.val == pred.val:
                curr.next = pred.next
                pred = None
                pred = curr.next
            # update curr and pred
            else:
                curr = pred
                pred = pred.next
        
        return head