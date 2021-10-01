# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        if head is None: return head
        
        odd = head
        even = head.next
        evenHead = even
        
        while even and even.next:
            # connect to next odd
            odd.next = even.next
            # update odd
            odd = odd.next
            # connect to next even
            even.next = odd.next
            # update even
            even = even.next
            
        # connect odd->even
        odd.next = evenHead
        
        return head
        