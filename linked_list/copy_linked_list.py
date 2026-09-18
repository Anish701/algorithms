from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        l1 = head
        while l1:
            l2 = Node(l1.val, l1.next)
            l1.next = l2
            l1 = l2.next
        
        l1 = head
        while l1:
            if l1.random:
                l1.next.random = l1.random.next
            l1 = l1.next.next

        l1, res = head, head.next
        while l1:
            l2 = l1.next
            l1.next = l1.next.next
            if l2.next:
                l2.next = l2.next.next
            l1 = l1.next

        return res
