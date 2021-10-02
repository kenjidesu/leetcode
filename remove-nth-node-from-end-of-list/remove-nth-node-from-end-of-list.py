# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        # count nodes
        i = 0
        curr = head
        while curr:
            curr = curr.next
            i += 1
        
        # return the next node
        if i == n:
            return head.next
        
        # remove nth node from end of list
        recur = head
        for _ in range(i-1, n, -1):
            recur = recur.next
            
        recur.next = recur.next.next
        
        return head
        
