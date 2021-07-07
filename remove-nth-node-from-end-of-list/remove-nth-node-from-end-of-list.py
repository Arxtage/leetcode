# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # two pointer
        # o(n) complexity, o(1) memory
        
        dummy = ListNode(0,head)
        left = dummy
        right = head
        
        while n > 0 and right:
            right = right.next
            n-=1
            
        while right:
            right = right.next
            left = left.next
            
        # deleting
        left.next = left.next.next
        return(dummy.next)