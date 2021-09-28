# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        arr = []
        curr = head
        while curr:
            # returns node if already visited
            if curr in arr:
                return curr
            # tracks the node visited
            arr.append(curr)
            curr = curr.next
            
        return None
        