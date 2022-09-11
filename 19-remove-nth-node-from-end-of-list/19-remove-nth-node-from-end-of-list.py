# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None: return head
        if n==1: 
            if head.next == None:
                return None

        curr = head
        prev = None
        count = -1
        while curr:
            count+=1
            if prev: prev= prev.next
            if count == n:
                prev = head
            curr = curr.next
        if prev:
            prev.next = prev.next.next
        else:
            return head.next
        return head