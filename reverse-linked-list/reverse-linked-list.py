# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        #o(n) speed & o(1) memory
        
        prev = None
        curr = head
        
        while curr:
            tmp_next = curr.next
            curr.next = prev
            prev = curr
            curr = tmp_next
        return(prev)