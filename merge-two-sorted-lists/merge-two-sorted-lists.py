# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        # create a dummynode
        dummyNode = ListNode(val=-1)
        head = dummyNode

        while l1 != None and l2 != None:
            # goes to the next of l1 if l1 < l2
            if l1.val < l2.val:
                dummyNode.next = l1
                l1 = l1.next
            # goes to the next of l2 if l2 > l1
            else:
                dummyNode.next = l2
                l2 = l2.next
            
            # updates the dummynode
            dummyNode = dummyNode.next
        
        # It appends the last val of l1 or l2
        if l1 != None:
            dummyNode.next = l1
        else:
            dummyNode.next = l2
        
        # returns the dummyNode without the -1
        return head.next