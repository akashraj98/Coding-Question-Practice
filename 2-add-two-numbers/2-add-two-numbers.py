# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = node = ListNode(0)
        
        while l1 or l2:
            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0
            carry,q = divmod(l1val+l2val+carry,10)
            node.next = ListNode(q)
            node = node.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry:
            node.next = ListNode(carry)
        return dummy.next
            
            
#         while l1 and l2:
#             q =l1.val+l2.val + carry
#             carry, q = divmod(q,10)
#             node.next = ListNode(q)
#             node = node.next
#             l1 = l1.next
#             l2 = l2.next
#         while l1:
#             q = l1.val+carry
#             carry, q = divmod(q,10)
#             node.next = ListNode(q)
#             node = node.next
#             l1 = l1.next
            
#         while l2:
#             q = l2.val+carry
#             carry, q = divmod(q,10)
#             node.next = ListNode(q)
#             node = node.next
#             l2 = l2.next
            
#         if carry:
#             node.next = ListNode(carry)
            
#         return dummy.next
        
        