from typing import List, Optional
from collections import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class NodeWrapper:
    def __init__(self, node=None):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists is None:
            return 0

        dummy = ListNode()
        itr = dummy
        minHeap = []

        for lst in lists:
            if lst is not None:
                heapq.heappush(minHeap, NodeWrapper(lst))
        
        while minHeap:
            tmp = heapq.heappop(minHeap)
            itr.next =  tmp.node
            itr = itr.next

            if tmp.node.next:
                nxt = NodeWrapper(tmp.node.next)
                heapq.heappush(minHeap, nxt)

        return dummy.next