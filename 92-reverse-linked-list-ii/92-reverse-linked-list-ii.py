# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummyNode = ListNode(0,head)
        curr = head
        prevleft = dummyNode      # This will handle ([5],1 ,1) case
        for _ in range(left-1):
            prevleft = curr
            curr = curr.next
        
        prev = None
        for _ in range(right-left+1):
            t = curr.next
            curr.next = prev
            prev = curr
            curr = t
        
        prevleft.next.next = curr
        prevleft.next = prev
        
        return dummyNode.next
        
        
            
                