"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
import copy
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        
        
        newHead = Node(head.val)
        curr = head.next
        currNew = newHead

        m = {head: newHead, None: None}
        while curr:
            cpHead = Node(curr.val)
            currNew.next = cpHead
            m[curr] = cpHead
            curr = curr.next
            currNew = currNew.next
        
        curr = head
        currNew = newHead

        while curr:
            currNew.random = m[curr.random]
            curr = curr.next
            currNew = currNew.next

        return newHead
            


