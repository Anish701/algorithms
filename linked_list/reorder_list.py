from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
	self.val = val
	self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow
        
        prev = None
        while mid:
            tmp = mid.next
            mid.next = prev
            prev = mid
            mid = tmp
        
        start = itr = ListNode()
        itr1, itr2 = head, prev
        while itr1 and itr2:
            itr.next = itr1
            itr1 = itr1.next
            itr = itr.next

            itr.next = itr2
            itr2 = itr2.next
            itr = itr.next
        itr.next = None

