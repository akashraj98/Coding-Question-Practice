# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pt1 = pt2 = head
        for _ in range(n):
            pt2 = pt2.next
        if not pt2:
            return head.next
        while pt2.next:
            pt1 = pt1.next
            pt2 = pt2.next
        pt1.next = pt1.next.next
        return head
        