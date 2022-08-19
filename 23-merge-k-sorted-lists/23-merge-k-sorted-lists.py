# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def greaterthan(self, other):
        if(self.val>other.val):
            return True
        else:
            return False
    ListNode.__gt__ = greaterthan
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        hp = []
        for head in lists:
            if head:
                heapq.heappush(hp,(head.val,head))
        ans = node = ListNode(0)
        while hp:
            el = heapq.heappop(hp)[1]
            node.next = el
            node = node.next
            if el.next:
                heapq.heappush(hp,(el.next.val,el.next))
            
        return ans.next