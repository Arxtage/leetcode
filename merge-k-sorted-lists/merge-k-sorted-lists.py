# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def merge_two_one(L, R):
    
    initial = ListNode()
    tail = initial
        
    while L and R:
        if L.val < R.val:
            tail.next = L
            L = L.next
        else:
            tail.next = R
            R = R.next
        tail = tail.next
        
    # дозаполнить остатки
    if L:
        tail.next = L
    else:
        tail.next = R
    
    return(initial.next)

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return(None)
        res = lists[0]
        for i in range(1, len(lists)):
            res = merge_two_one(res, lists[i])
        return(res)