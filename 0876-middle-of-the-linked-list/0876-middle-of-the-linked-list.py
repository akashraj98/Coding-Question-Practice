# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        nxt = head
        while nxt.next and nxt.next.next:
            curr = curr.next
            nxt = nxt.next.next
        return curr.next if nxt.next else curr
        