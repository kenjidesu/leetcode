# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        if head is None: return head
        
        prev = None
        curr = head
        while curr:
            # we get rid of the first elements
            # prev is None, it means that's the first element
            if curr.val == val and prev is None:
                head = curr.next
                curr = curr.next
            # we connect the prev node to the curr.next
            # basically we're removing the val in the linked list
            elif curr.val == val and prev is not None:
                prev.next = curr.next
                curr = prev.next
            # update prev and curr
            else:
                prev = curr
                curr = curr.next
                
        return head