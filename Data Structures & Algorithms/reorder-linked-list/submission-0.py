# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import copy

class Solution:

    def reverse(self, head):
        if not head:
            return head

        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev

    def merge(self, head1, head2, isFirst = True):
        if not head1:
            return head2

        if not head2:
            return head1

        head = ListNode(head1.val if isFirst else head2.val)
        if isFirst:
            head.next = self.merge(head1.next, head2, not isFirst)
        else:
            head.next = self.merge(head1, head2.next, not isFirst)

        return head
        


    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head:
            return
        
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        first = head
        second = slow.next
        slow.next = None

        second = self.reverse(second)

        isFirst = True
        


        while second:
            next1 = first.next
            next2 = second.next

            first.next = second
            second.next = next1

            first = next1
            second = next2
            
            




