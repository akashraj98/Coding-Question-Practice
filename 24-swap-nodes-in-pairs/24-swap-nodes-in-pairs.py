# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        curr = head
        prev = None
        start = head.next
        while curr and curr.next:
            nxt = curr.next
            curr.next = nxt.next
            nxt.next = curr
            if prev: prev.next = nxt
            prev = curr
            curr = curr.next
        return start
            