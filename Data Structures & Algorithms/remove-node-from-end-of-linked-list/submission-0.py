# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def length(self, head):
        if not head:
            return 0

        return 1 + self.length(head.next)

    def remove(self, head, idx):
        if idx == 0:
            return head.next if head else None

        head.next = self.remove(head.next, idx - 1)
        
        return head

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        idx = self.length(head) - n
        return self.remove(head, idx)
