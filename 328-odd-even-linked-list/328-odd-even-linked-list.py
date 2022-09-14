# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        oddHead = odd = ListNode(0)
        evenHead = even = ListNode(0)
        isodd = True
        while head:
            if isodd:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next
            isodd = not isodd
            head = head.next
        
        even.next = None
        odd.next = evenHead.next
        return oddHead.next
        