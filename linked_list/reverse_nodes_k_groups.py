from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        prevLast = dummy

        while True:
            knode = prevLast
            for i in range(k):
                knode = knode.next
                if not knode:
                    return dummy.next
            
            nextFirst = knode.next

            prev = nextFirst
            itr = prevLast.next
            while itr is not nextFirst:
                tmp = itr.next
                itr.next = prev
                prev = itr
                itr = tmp

            tmp = prevLast.next
            prevLast.next = prev
            prevLast = tmp
