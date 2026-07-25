# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def merge(self, l, r):
        if not l:
            return r

        if not r:
            return l
        t = ListNode(min(l.val, r.val))
        if(l.val <= r.val):
            t.next = self.merge(l.next, r)
        else:
            t.next = self.merge(l, r.next)
        
        return t
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        return self.merge(list1, list2)