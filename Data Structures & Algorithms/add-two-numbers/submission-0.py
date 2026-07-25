# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def helper(self, l1, l2, carry = 0):
        if not l1 and not l2:
            return ListNode(carry) if carry else None

        val = carry + (l1.val if l1 else 0) + (l2.val if l2 else 0)
        node = ListNode(val % 10)
        carry = val // 10

        node.next = self.helper(l1.next if l1 else None, l2.next if l2 else None, carry)
        return node

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.helper(l1, l2)