# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummyNode = ListNode(0,head)
        leftpt = head
        prevleft = dummyNode      # This will handle [5],1 ,1 case
        for _ in range(left-1):
            prevleft = leftpt
            leftpt = leftpt.next
        
        prev = None
        rightpt = leftpt
        for _ in range(right-left+1):
            t = leftpt.next
            leftpt.next = prev
            prev = leftpt
            leftpt = t
        
        prevleft.next.next = leftpt
        prevleft.next = prev
        
        return dummyNode.next
        
        
            
                