# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        vals = []
        cpy = head
        nn = head
        
        # gets all the value of Linked-list
        while nn:
            vals.append(nn.val)
            nn = nn.next
        
        # updates the val of head
        i = len(vals)-1
        while cpy:
            cpy.val = vals[i]
            cpy = cpy.next
            i -= 1
            
        return head
        
        