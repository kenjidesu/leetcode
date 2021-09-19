# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        curA, curB = headA, headB
        th_a, th_b = 0, 0
        
        # gets length of headA
        while curA:
            th_a += 1
            curA = curA.next
        
        # gets length of headB
        while curB:
            th_b += 1
            curB = curB.next
        
        # gets which is longer and shorter linked-list
        if th_a > th_b:
            curL = headA
            curS = headB
        else:
            curL = headB
            curS = headA
        
        # gets the gap of longer and shorter linked-list
        diff = abs(th_a - th_b)
        
        # advanced the longer one to match the shorter linked-list
        for i in range(diff):
            curL = curL.next
            
        while curL and curS:
            # checks whether there is an intersection
            if curS == curL:
                return curS
            curL = curL.next
            curS = curS.next
        
        return None