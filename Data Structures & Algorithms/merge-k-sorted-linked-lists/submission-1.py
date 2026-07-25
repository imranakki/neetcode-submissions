# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import sys
sys.setrecursionlimit(1 << 30)
class Solution:    
    def merge(self, l1, l2):
        if not l1:
            return l2
        
        if not l2:
            return l1

        node = ListNode(min(l1.val, l2.val))
        if l1.val <= l2.val:
            node.next = self.merge(l1.next, l2)
        else:
            node.next = self.merge(l1, l2.next)

        return node
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        node = None
        for e in lists:
            node = self.merge(node, e)
        return node