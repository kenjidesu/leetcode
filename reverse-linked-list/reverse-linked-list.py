# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        # checks if head exists
        if head is None:
            return head
        
        curr = head
        sec = head.next
        
        # reverse nodes
        while curr and sec:
            # connect to the next of sec
            curr.next = sec.next
            # connect to the head
            sec.next = head
            # set a new head
            head = sec
            # update sec
            sec = curr.next
        
        return head
        