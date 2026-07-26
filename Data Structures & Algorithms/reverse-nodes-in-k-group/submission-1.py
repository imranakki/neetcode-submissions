# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def length(self, node):
        if not node:
            return 0

        return 1 + self.length(node.next)

    def findKth(self, node, k):
        if not node:
            return node

        if k == 1:
            return node

        return self.findKth(node.next, k - 1)
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = self.length(head)
        start = head
        R = self.findKth(head, ((n // k) * k ) + 1)
        prev, curr = None, start
        dummy = None
        begenning = None
        for _ in range(n // k):
            cnt = k
            prev, curr = None, start
            while curr and cnt:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                cnt -= 1
            
            if dummy:
                dummy.next = prev

            if not begenning:
                begenning = prev
            dummy = start
            start = curr

        curr = begenning
        while curr.next:
            curr = curr.next

        curr.next = R
        print(curr.next)
        return begenning
                

        

            