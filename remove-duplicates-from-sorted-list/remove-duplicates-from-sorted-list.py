# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # O(N) Two pointers
        
        if not head:
            return head
        saved = head
        L = head
        R = head
        
        while R.next:
            R = R.next
            if L.val == R.val:
                continue
            else:
                L.next = R
                L = L.next
                
        if L != R:
            L.next = None
        return saved