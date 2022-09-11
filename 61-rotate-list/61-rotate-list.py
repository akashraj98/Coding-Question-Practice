# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        curr = head
        stack =[]
        while curr:
            stack.append(curr)
            curr = curr.next
        
        for i in range(k%len(stack)):
            node = stack.pop()
            node.next = head
            head = node
            stack[-1].next = None
        return head
            