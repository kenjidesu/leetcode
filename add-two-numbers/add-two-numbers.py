# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    """
    Explanation:
    https://leetcode.com/problems/add-two-numbers/solution/
    """
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(-1)
        curr = dummy
        carry = 0
        p = l1
        q = l2
        
        while p or q:
            x = p.val if p is not None else 0
            y = q.val if q is not None else 0
            sm = x + y + carry
            carry = sm / 10
            curr.next = ListNode(sm % 10)
            curr = curr.next
            if p is not None: p = p.next
            if q is not None: q = q.next
            
        if carry:
            curr.next = ListNode(1)
            
        return dummy.next
        