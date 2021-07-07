# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # o(n) complexity, o(1) memory
        if head.next == None:
            return(None)
        curr = head
        counter = 0
        while curr:
            counter +=1
            curr = curr.next
        
        if n == counter:
            return(head.next)
        num = 1
        prev = head
        prev_source = prev
        curr = head.next
        while num != counter-n:
            num+=1
            curr = curr.next
            prev = prev.next
        
        curr = curr.next
        prev.next = curr
        return(prev_source)