# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        #o(n) speed & memory
        if not head:
            return(head)
        new = ListNode(head.val, None)
        head = head.next
        prev = new
        
        while True:
            if head == None:
                break
            new = ListNode(head.val, prev)
            head = head.next
            prev = new
        return(new)
            