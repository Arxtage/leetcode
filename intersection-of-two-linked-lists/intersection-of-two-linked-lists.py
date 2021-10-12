# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # O(n+m)  O(n)
        
        hashsetA = set()
        
        while headA != None and headB != None:
            hashsetA.add(headA)
            headA = headA.next
        
        while headB != None:
            if headB in hashsetA:
                return headB
            headB = headB.next
        return None