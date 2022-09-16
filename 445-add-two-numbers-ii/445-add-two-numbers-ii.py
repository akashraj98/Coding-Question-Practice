# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_s = []
        l2_s = []
        while l1:
            l1_s.append(l1)
            l1 = l1.next
        while l2:
            l2_s.append(l2)
            l2 = l2.next
        dummy = ListNode(-1)
        carry,prev = 0,None
        while l1_s or l2_s or carry: 
            n1 = l1_s.pop().val if l1_s  else 0
            n2 = l2_s.pop().val if l2_s  else 0
            carry,q = divmod(n1+n2+carry,10)
            dummy.next = ListNode(q)
            t = dummy.next
            if dummy.val >=0: # reverse if its is not dummynode -1
                dummy.next = prev
                prev = dummy
            dummy = t
        # for last element reverse link
        dummy.next = prev
        prev = dummy
        return prev


# carry,head = 0,None
#         while l1_s or l2_s or carry:
#             n1 = l1_s.pop().val if l1_s  else 0
#             n2 = l2_s.pop().val if l2_s  else 0
#             carry,q = divmod(n1+n2+carry,10)
#             head = ListNode(q,head)
#         return head
            
            
            