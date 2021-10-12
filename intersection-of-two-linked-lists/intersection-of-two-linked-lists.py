# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pA = headA
        pB = headB

        while pA != pB:
            
            if pA is None:
                pA = headB
            else:
                pA = pA.next
                
            if pB is None:
                pB = headA 
            else:
                pB = pB.next   

        return pA