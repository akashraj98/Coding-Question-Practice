# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        d1head =dummy1 = ListNode(0)
        d2head =dummy2 = ListNode(0)
        curr = head
        while curr:
            if curr.val <x:
                dummy1.next = curr
                curr = curr.next
                dummy1 =dummy1.next
            else:
                dummy2.next = curr
                curr = curr.next
                dummy2 = dummy2.next
        dummy1.next = d2head.next
        if dummy2:
            dummy2.next = None
        return d1head.next
        