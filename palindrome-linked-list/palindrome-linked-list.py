# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        palin = []
        curr = head
        # gets all the val of linked list and append it to palin
        while curr:
            palin.append(curr.val)
            curr = curr.next
            
        # compares the non-reverse and reverse nodes element
        return palin == palin[::-1]